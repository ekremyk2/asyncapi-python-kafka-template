from confluent_kafka import Producer
from confluent_kafka import Consumer
{% for channel_id, channel_info in asyncapi.channels() -%}
from topics.{{ channel_id }} import {{ channel_id }}Consumer, {{ channel_id }}Producer
{% endfor -%}

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers[0].url }}'

# Create a Kafka consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

{% for channel_id, channel_info in asyncapi.channels() -%}
# Subscribe to the Kafka topic for {{ channel_name }} channel
{{ channel_id|lower }}_topic = '{{ channel_info.subscribe().topic }}'
consumer.subscribe([{{ channel_id|lower }}_topic])

# Create a {{ channel_name }} consumer and start consuming messages
{{ channel_id|lower }}_consumer = {{ channel_id }}Consumer(KAFKA_BROKERS, {{ channel_id|lower }}_topic, consumer)
{{ channel_id|lower }}_consumer.consume_messages()

# Create a {{ channel_name }} producer and send a message
{{ channel_id|lower }}_producer = {{ channel_id }}Producer(KAFKA_BROKERS, {{ channel_id|lower }}_topic, producer)
{{ channel_id|lower }}_producer.produce_message('Hello, World!')
{% endfor -%}