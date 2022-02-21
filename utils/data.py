from enum import Enum
from aenum import MultiValueEnum


class Urls(Enum):
    BASE_URL = 'https://apex.heits.digital/'
    ENGINEERING_URL = 'https://apex.heits.digital/engineering'


class MenuItems(MultiValueEnum):
    """
    MultiValueEnum enables tuple values in enum configuration
    e.g. MenuItems.Machine_Learning.values[0] returns 'Machine learning'
    e.g. MenuItems.Machine_Learning.values[1] returns 'https://apex.heits.digital/machine-learning'
    """
    MACHINE_LEARNING = 'Machine learning', 'https://apex.heits.digital/machine-learning'
    DIGITAL_SOFTWARE_DEVELOPMENT = 'Digital software development', 'https://apex.heits.digital/software-development'
    USER_EXPERIENCE = 'User experience', 'https://apex.heits.digital/user-experience'
    CULTURE = 'Culture', 'https://apex.heits.digital/culture'
    OUR_WORK = 'Our work', 'https://apex.heits.digital/work'
    ENGAGEMENT_MODELS = 'Engagement models', 'https://apex.heits.digital/engagement'
    LETS_CHAT = 'Let’s chat'
