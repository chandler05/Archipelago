from .names import Items as I

MEMORY_START = 0x80000000

class CreatureData:
    def __init__(self, offset, originalAdd, modAdd):
        self.offset = offset
        self.originalAdd = originalAdd
        self.modAdd = modAdd

creature_offsets = {
    I.SNAKE: CreatureData(0x47bc4, 0x41820050, 0x48000050),
    I.CENTIPEDE: CreatureData(0x451f4, 0x41820058, 0x48000058),
    I.BAT: CreatureData(0x5ccc8, 0x4182004c, 0x4800004c),
    I.FROG: CreatureData(0X51588, 0x4182004c, 0x4800004c),
    I.WORM: CreatureData(0x53f48, 0x4182004c, 0x4800004c),
    I.GOBLIN: CreatureData(0x58b2c, 0x4182004c, 0x4800004c), #MAKE THIS TWO LATER
    I.KING_GROWL: CreatureData(0x6abc4, 0x41820078, 0x48000078),
}

GECKO_CODE_ADR = 0x80002340
GECKO_CODE_INS = 0x80002344
GECKO_CODE_START = 0x04000000