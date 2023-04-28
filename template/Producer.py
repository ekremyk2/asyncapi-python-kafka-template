from confluent_kafka import Producer
import threading


class Producer:
    __instance = None
    producer = None

    def __new__(self, broker_url: str):
        if self.__instance is None:
            self.__instance = self.createInstance(broker_url)
            return self.__instance
        else:
            raise Exception(
                "Cannot create more than one instance of a singleton class.")

    def createInstance(self, broker_url: str):
        self.producer = Producer({'bootstrap.servers': broker_url})

    def produce_message(self, topic: str, message: str):
        if self.producer is None:
            raise Exception("Producer intance should be initialized first!")
        self.producer.produce(topic, message.encode('utf-8'))
        """, callback = delivery_report"""
        self.producer.flush()
