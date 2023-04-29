from kafka_utils.kafka_decorator import on
from kafka_utils.kafka_enum import KafkaAction
import logging

class KafkaConsumer():
    def __init__(self, broker_url: str, group_id: str):
        super().__init__(broker_url, group_id)
        
{% for channel_name, channel in asyncapi.channels() %}
{% if channel.hasPublish() %}
{% for message_name, message in channel.messages() %}
{{"    "}}@on(KafkaAction.{{ message_name | camelCase }})
{{"    "}}async def on_{{ message_name | capitalize }}(self,{% for name, prop in message.payload().properties() %}{{ name }},{% endfor %}, **kwargs ):
{{"    "}}{{"    "}}logging.warning("{% for name, prop in message.payload().properties() %}{{ name }}: %s, {% endfor %}", {% for name, prop in message.payload().properties() %}{{ name }}{% endfor %})
{{"    "}}{{"    "}}return kafka_result.{{ message.payload()["schema_name"] }}(
{% for name, prop in message.payload().properties() %}
{{"    "}}{{"    "}}{{"    "}}{{ name }} = {{ name }},
{% endfor %}
{{"    "}}{{"    "}})
{% endif %}
{% endfor %}
{% endfor %}