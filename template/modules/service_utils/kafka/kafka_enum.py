from enum import Enum

{% for schema_name, schema in asyncapi.components().schemas() %}
{% for name, prop in schema.properties() %}
{% set tpyeInfo = [name, prop] | getTypeInfo %}
{% if typeInfo.generalType === 'enum' %}
class {{schema_name}}(str, Enum):
{% for v in typeInfo.enum %}
{{"    "}}{{ v }} = '{{ v }}'
{% endfor %}
{% endif %}
{% endfor %}        
{% endfor %}