from confluent_kafka import Consumer
import logging

logger = logging.getLogger("Kafka")


class KafkaConsumer:

    consumer = None

    def __init__(self, broker_url: str, group_id: str):
        self.consumer = Consumer({
            'bootstrap.servers': broker_url,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })
        logger.info("Consumer instance created!")

    def subscribeTo(self, topic: str):
        if topic is None:
            logger.error("Topic is None!")
        self.consumer.subscribe([topic])
        logger.info(f"Subscribed to {topic} topic!")

    def listen(self, callback):
        if callback is None:
            logger.error("Callback is None!")
        try:
            while True:  # INFO: You can add a condition to stop the loop
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    logger.error(f'Message Error! Message: {msg.error()}')
                    continue
                logger.info(f'Message received: {msg.value().decode("utf-8")}')
                callback(msg)
                self.consumer.commit()
        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt!")
        except Exception as e:
            logger.error(f"Exception occured: {e}")
        finally:
            self.consumer.close()
            logger.info("Consumer closed!")
