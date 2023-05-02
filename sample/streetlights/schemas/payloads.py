import json
from enum import Enum

class Entity():
    @classmethod
    def from_json(cls, data):
        jsonObj = json.loads(data)
        return cls(**jsonObj)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)

class turnOnOffPayload(Entity):
    class Command(str, Enum):
        on = 'on'
        off = 'off'
    
    def __init__(self,command: Command, sentAt: str, ):
        self.command = command
        self.sentAt = sentAt
        
class dimLightPayload(Entity):
    
    def __init__(self,percentage: int, sentAt: str, ):
        self.percentage = percentage
        self.sentAt = sentAt
        