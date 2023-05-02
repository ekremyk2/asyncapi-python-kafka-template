import json
from enum import Enum

class Entity():
    @classmethod
    def from_json(cls, data):
        jsonObj = json.loads(data)
        return cls(**jsonObj)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)
{% set messagePayloads = asyncapi | getDistinctPayloadsWithSchemaId %}{% for key, value in messagePayloads %}
class {{key}}(Entity):{% for name, prop in value.properties() %}{% set typeInfo = [name, prop] | getTypeInfo %}{% if typeInfo.generalType === 'enum' %}
{{"    "}}class {{typeInfo.pythonName | pascalCase }}(str, Enum):{% for v in typeInfo.enum %}
{{"    "}}{{"    "}}{{v }} = '{{ v }}'{% endfor %}{% endif %}{% endfor %}
{{"    "}}
{{"    "}}def __init__(self,{% for name, prop in value.properties() %}{% set typeInfo = [name, prop] | getTypeInfo %}{{ typeInfo.pythonName }}{{ ": " + typeInfo.pythonType if typeInfo.pythonType else ""}}, {% endfor %}):{% for name, prop in value.properties() %}{% set typeInfo = [name, prop] | getTypeInfo %}
{{"    "}}{{"    "}}self.{{ name }} = {{ name }}{% endfor %}
{{"    "}}{{"    "}}{% endfor %}