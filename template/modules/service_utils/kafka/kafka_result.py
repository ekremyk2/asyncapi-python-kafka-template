from dataclasses import dataclass
from kafka.kafka_result import *

{% for schema_name, schema in asyncapi.components().schemas() -%}
@dataclass
class {{schema_name}}:
{% for name, prop in schema.properties() %}
{% set typeInfo = [name, prop] | getTypeInfo -%}
{{"    "}}{{ typeInfo.pythonName }}{{ ": " + typeInfo.pythonName if typeInfo.pythonName else ""}}
{%- else %}
{{"    "}}pass
{% endfor %}
{% endfor %}