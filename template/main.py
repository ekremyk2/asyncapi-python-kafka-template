from Consumer import consumer
from Producer import producer

{% for channel_name, channel in asyncapi.channels() -%}
{% if channel.hasSubscribe() -%}
{% endif -%}
{% endfor %}

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers().test._json.url }}'

# Create a Kafka consumer
consumerInstance = consumer({
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'my-group',
})

# Create a Kafka producer
producerInstance = producer({
    'bootstrap.servers': KAFKA_BROKERS
})

{% for channel_name, channel in asyncapi.channels() -%}
{% if channel.hasSubscribe() -%}
# Subscribe to the Kafka topic for {{ channel_name }} channel
consumerInstance.subscribeTo('{{ channel_name }}')
{% endif -%}
{% endfor %}


def listenCallback(msg: str):
    # Write your business logic here
    {% for channel_name, channel in asyncapi.channels() -%}
    {% if channel.hasPublish() -%}
    # Produce messages to Kafka topic for {{ channel_name }} channel
    {% endif -%}    
    {% endfor %}
    # producerInstance.produce_message("topic", Entity)
    print(msg)
    return


consumerInstance.listen(listenCallback)
