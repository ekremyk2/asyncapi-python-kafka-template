from confluent_kafka import Producer
from schemas import entity
import threading


class producer:
    __instance = None
    producer = None

    def __new__(cls, broker_url: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__init__(broker_url)
            return cls.__instance
        else:
            raise Exception(
                "Cannot create more than one instance of a singleton class.")

    def __init__(self, broker_url: str):
        self.producer = Producer({'bootstrap.servers': broker_url})

    def produce_message(self, topic: str, message: entity):
        if self.producer is None:
            raise Exception("Producer intance should be initialized first!")
        msgJson = message.to_json()
        self.producer.produce(topic, msgJson.encode('utf-8'))
        """, callback = delivery_report"""
        self.producer.flush()
