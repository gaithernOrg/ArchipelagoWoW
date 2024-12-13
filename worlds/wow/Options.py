from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup

class HonorInPool(Range):
    """
    Determines the amount of Honor in the pool.
    """
    display_name = "Honor in Pool"
    default = 10
    range_start = 5
    range_end = 20

class HonorToWin(Range):
    """
    Determines the amount of Honor to achieve victory.
    """
    display_name = "Honor to Win"
    default = 5
    range_start = 5
    range_end = 30

@dataclass
class WOWOptions(PerGameCommonOptions):
    honor_in_pool: HonorInPool
    honor_to_win: HonorToWin

WOW_option_groups = [
    OptionGroup("Etc", [
        HonorInPool,
        HonorToWin,
    ])
]
