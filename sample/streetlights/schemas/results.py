from schemas.enum import *

class lightMeasuredPayload:
    lumens: int
    sentAt: str

class turnOnOffPayload:
    command: Command
    sentAt: str

class dimLightPayload:
    percentage: int
    sentAt: str

class sentAt:
    pass

