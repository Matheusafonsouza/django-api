from enum import Enum


class BaseEnum(Enum):
    """
    Base class for all enums over the application.
    """
    @classmethod
    def choices(cls):
        return (tuple((i.name, i.value) for i in cls))
