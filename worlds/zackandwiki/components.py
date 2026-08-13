from worlds.LauncherComponents import Component, Type, components, launch

from worlds.zackandwiki.names import Game

def run_client(*args: str) -> None:
    from .client import launch_client

    launch(launch_client, name="Zack & Wiki Client", args=args)

components.append(
    Component(
        "Zack & Wiki Client",
        func=run_client,
        game_name=Game.GAME,
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)