import template.Consumer as Consumer
import template.Producer as Producer
{% for channel_name, channel_info in asyncapi.channels() - %}
from topics import {{channel_name}}
{% endfor - %}

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers[0].url }}'

# Create a Kafka consumer
consumerInstance = Consumer({
    'bootstrap.servers': KAFKA_BROKERS,
    'group.id': 'my-group',
})

producerInstance = Producer({
    'bootstrap.servers': KAFKA_BROKERS
})

{% for channel_name, channel_info in asyncapi.channels() - %}
# Subscribe to the Kafka topic for {{ channel_name }} channel
consumerInstance.subscribeTo('{{ channel_info.subscribe().topic }}')
{% endfor - %}


def listenCallback(msg: str):
    #write your business logic hereks
    return


consumerInstance.listen(listenCallback)
