from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, OptionGroup

class Placeholder(Toggle):
    """
    Placeholder
    """
    display_name = "Placeholder"

@dataclass
class WOWOptions(PerGameCommonOptions):
    placeholder: Placeholder

WOW_option_groups = [
    OptionGroup("Etc", [
        Placeholder,
    ])
]
