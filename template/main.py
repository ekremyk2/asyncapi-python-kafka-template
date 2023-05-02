from schemas.{{schema_name}} import {{schema_name}}
from utils.consumer import KafkaConsumer
from utils.producer import KafkaProducer
from schemas.payloads import *

# Set up Kafka configuration
KAFKA_BROKERS = '{{ asyncapi.servers().test._json.url }}'

# Create a Kafka consumer
Consumer = KafkaConsumer(KAFKA_BROKERS, 'my-group')

# Create a Kafka producer
Producer = KafkaProducer(KAFKA_BROKERS)

{% for channel_name, channel in asyncapi.channels() %}{% if channel.hasSubscribe() %}
# Subscribe to the Kafka topic for {{ channel_name }} channel
Consumer.subscribeTo('{{ channel_name }}')
{% endif %}{% endfor %}

def listenCallback(msg: str):
    # Write your business logic here

    {% for channel_name, channel in asyncapi.channels() %}{% if channel.hasPublish() %}
    # Produce messages to Kafka topic for {{ channel_name }} channel
    {% endif %}{% endfor %}

    # producerInstance.produce_message("topic", Entity)
    print(msg)
    return

Consumer.listen(listenCallback)
