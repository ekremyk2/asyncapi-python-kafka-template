import template.Consumer as Consumer
import template.Producer as Producer

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers[0].url }}'

# Create a Kafka consumer
consumerInstance = Consumer({
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'my-group',
})

# Create a Kafka producer
producerInstance = Producer({
    'bootstrap.servers': KAFKA_BROKERS
})

{% for channel_name, channel_info in asyncapi.channels() %}
# Subscribe to the Kafka topic for {{ channel_name }} channel
consumerInstance.subscribeTo('{{ channel_info.subscribe().topic }}')
{% endfor %}


def listenCallback(msg: str):
    # Write your business logic here
    # producerInstance.produce_message("topic", "message")
    print(msg)
    return


consumerInstance.listen(listenCallback)
