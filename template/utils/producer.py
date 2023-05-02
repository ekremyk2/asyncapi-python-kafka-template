from confluent_kafka import Producer
from schemas.payloads import Entity
import logging

logger = logging.getLogger("Kafka")


class KafkaProducer:
    producer = None

    def __init__(self, broker_url: str):
        self.producer = Producer({'bootstrap.servers': broker_url})
        logger.info("Producer instance created!")

    def produce_message(self, topic: str, message: Entity):
        if topic is None:
            logger.error("Topic is None!")
            return
        if message is None:
            logger.error("Message is None!")
            return
        try:
            msgJson = message.to_json()
            self.producer.produce(topic, msgJson.encode('utf-8'))
        except Exception as e:
            logger.error(f"Exception occured: {e}")
        finally:
            self.producer.flush()
            logger.info(f"Message produced to {topic} topic!")
