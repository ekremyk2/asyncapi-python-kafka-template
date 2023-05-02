from schemas.enum import *

{% for schema_name, schema in asyncapi.components().schemas() -%}

class {{schema_name}}:{% for name, prop in schema.properties() %}
{% set typeInfo = [name, prop] | getTypeInfo -%}
{{"    "}}{{ typeInfo.pythonName }}{{ ": " + typeInfo.pythonType if typeInfo.pythonType else ""}}{%- else %}
{{"    "}}pass{% endfor %}

{% endfor %}