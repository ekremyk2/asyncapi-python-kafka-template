from utils.consumer import KafkaConsumer
from utils.producer import KafkaProducer
from schemas.payloads import *

# Set up Kafka configuration
KAFKA_BROKERS = 'test.mosquitto.org:{port}'

# Create a Kafka consumer
Consumer = KafkaConsumer(KAFKA_BROKERS, 'my-group')

# Create a Kafka producer
Producer = KafkaProducer(KAFKA_BROKERS)


# Subscribe to the Kafka topic for smartylighting/streetlights/1/0/action/{streetlightId}/turn/on channel
Consumer.subscribeTo('smartylighting/streetlights/1/0/action/{streetlightId}/turn/on')

# Subscribe to the Kafka topic for smartylighting/streetlights/1/0/action/{streetlightId}/turn/off channel
Consumer.subscribeTo('smartylighting/streetlights/1/0/action/{streetlightId}/turn/off')

# Subscribe to the Kafka topic for smartylighting/streetlights/1/0/action/{streetlightId}/dim channel
Consumer.subscribeTo('smartylighting/streetlights/1/0/action/{streetlightId}/dim')



def listenCallback(msg: str):
    # Write your business logic here
    # Producer.produce_message("topic", Entity)
    
    # Produce messages to Kafka topic for smartylighting/streetlights/1/0/event/{streetlightId}/lighting/measured channel
    
    print(msg)
    return


Consumer.listen(listenCallback)
