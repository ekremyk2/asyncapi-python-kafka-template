from enum import Enum

class Command(str, Enum):
    on = 'on'
    off = 'off'