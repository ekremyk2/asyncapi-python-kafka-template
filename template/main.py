from topics.{{channel_name}} import {{channel_name}}Consumer, {{channel_name}}Producer
from confluent_kafka import Producer
from confluent_kafka import Consumer
{%- for channel_name, channel_info in asyncapi.channels() %}
{%- endfor %}

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers[0].url }}'

# Create a Kafka consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

{%- for channel_name, channel_info in asyncapi.channels() %}
# Subscribe to the Kafka topic for {{ channel_name }} channel
{{channel_name | lower}}_topic = '{{ channel_info.subscribe().topic }}'
consumer.subscribe([{{channel_name | lower}}_topic])

# Create a {{ channel_name }} consumer and start consuming messages
{{channel_name | lower}}_consumer = {{channel_name}}Consumer(KAFKA_BROKERS, {{channel_name | lower}}_topic, consumer)
{{channel_name | lower}}_consumer.consume_messages()

# Create a {{ channel_name }} producer and send a message
{{channel_name | lower}}_producer = {{channel_name}}Producer(KAFKA_BROKERS, {{channel_name | lower}}_topic, producer)
{{channel_name | lower}}_producer.produce_message('Hello, World!')
{%- endfor % }
