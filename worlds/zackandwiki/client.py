import asyncio
import colorama
import Utils
import kvui
import traceback

from collections.abc import Sequence
from typing import Any, Dict, Optional

import dolphin_memory_engine as dme

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, handle_url_arg, gui_enabled, server_loop, logger
from worlds.LauncherComponents import launch
from .names import Game as G, Dolphin as D, Items as I
from .items import ITEM_NAME_TO_ID, item_table
from .addresses import GECKO_CODE_ADR, GECKO_CODE_INS, GECKO_CODE_START, MEMORY_START, creature_offsets


def main(*args: str) -> None:
    Utils.init_logging("Zack & Wiki Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = ZaWContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        # Wake the sync task, if it is currently sleeping, so it can start shutting down when it sees that the
        # exit_event is set.
        ctx.watcher_event.set()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

    parser = get_base_parser()
    parsed_args = parser.parse_args(args)

    import colorama

    colorama.init()
    asyncio.run(_main(parsed_args.connect, parsed_args.password))
    colorama.deinit()

class ZaWCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        if isinstance(self.ctx, ZaWContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

class ZaWContext(CommonContext):
    command_processor = ZaWCommandProcessor
    game: str = G.GAME
    items_handling: int = 0b111

    instructions: Dict[hex, hex] = {}

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = D.CONNECTION_INITIAL_STATUS

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        self.auth = None
        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def get_username(self):
        if not self.auth:
            self.auth = self.username
            if not self.auth:
                logger.info('Enter slot name:')
                self.auth = await self.console_input()

    async def enable_bell(self):
        allItems: list[int] = []
        for item in self.items_received:
            name = self.item_names.lookup_in_game(item.item)
            itemID = ITEM_NAME_TO_ID[name]
            allItems.append(itemID)

        for creature in creature_offsets:
            if item_table[creature].id in allItems:
                if dme.read_word(MEMORY_START + creature_offsets[creature].offset) != creature_offsets[creature].originalAdd:
                    self.instructions.update({creature_offsets[creature].offset: creature_offsets[creature].originalAdd})
            else:
                if dme.read_word(MEMORY_START + creature_offsets[creature].offset) != creature_offsets[creature].modAdd:
                    self.instructions.update({creature_offsets[creature].offset: creature_offsets[creature].modAdd})

    async def modify_instructions(self):
        if len(self.instructions) > 0:
            add = next(iter(self.instructions))
            ins = self.instructions[add]
            dme.write_word(GECKO_CODE_ADR, GECKO_CODE_START + add)
            dme.write_word(GECKO_CODE_INS, ins)
            self.instructions.pop(add)
            self.sleep_time = 0.1

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        return
        #if cmd == "Connected":
            

    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Archipelago Zack & Wiki: Quest for Barbaros' Treasure"
        return ui

def launch_client(*args: Sequence[str]) -> None:
    launch(main, name="ZackAndWikiClient", args=args)

async def dolphin_sync_task(ctx: ZaWContext) -> None:
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time = 0.0
    while not ctx.exit_event.is_set():
        if sleep_time > 0.0:
            try:
                await asyncio.wait_for(ctx.watcher_event.wait(), sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()
        try:
            if dme.is_hooked() and ctx.dolphin_status == D.CONNECTION_CONNECTED_STATUS:
                if not check_in_rom():
                    sleep_time = 0.1
                    continue
                if ctx.slot is not None:
                    # Loop
                    await ctx.enable_bell()
                    await ctx.modify_instructions()
                sleep_time = 0.1
            else:
                if ctx.dolphin_status == D.CONNECTION_CONNECTED_STATUS:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = D.CONNECTION_LOST_STATUS
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    if dme.read_bytes(0x80000000, 6) != b"RTZE08":
                        logger.info(D.CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = D.CONNECTION_REFUSED_GAME_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    else:
                        logger.info(D.CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = D.CONNECTION_CONNECTED_STATUS
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = D.CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    sleep_time = 5
                    continue
        except Exception:
            dme.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = D.CONNECTION_LOST_STATUS
            await ctx.disconnect()
            sleep_time = 5
            continue

def check_in_rom() -> bool:
    try:
        dme.read_bytes(0x80000000, 6)
    except RuntimeError:
        if dme.is_hooked():
            dme.un_hook()
        return False
    return True