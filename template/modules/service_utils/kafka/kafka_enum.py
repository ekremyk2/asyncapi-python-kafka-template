from enum import Enum

{% for schema_name, schema in asyncapi.components().schemas() %}
{% for name, prop in schema.properties() %}
{% set typeInfo = [name, prop] | getTypeInfo %}
{% if typeInfo.generalType === 'enum' %}
class {{ typeInfo.pythonName }}(str, Enum):
{% for v in typeInfo.enum %}
{{"    "}}{{ v }} = '{{ v }}'
{% endfor %}
{% endif %}
{% endfor %}        
{% endfor %}