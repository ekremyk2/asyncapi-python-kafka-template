{% from "partials/model-class" import modelClass -%}
from enum import Enum
from schemas.Entity import Entity
{% set imports = schema | getImports %}
{{ imports }}
{{ modelClass(schemaName, schema.properties(), schema.required(), 0 ) }}
