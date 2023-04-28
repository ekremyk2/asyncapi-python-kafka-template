from confluent_kafka import Consumer
import threading


class consumer:
    __instance = None
    consumer = None

    def __new__(cls, broker_url: str, group_id: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__init__(broker_url, group_id)
            return cls.__instance
        else:
            raise Exception(
                "Cannot create more than one instance of a singleton class.")

    def __init__(self, broker_url: str, group_id: str):
        self.consumer = Consumer({
            'bootstrap.servers': broker_url,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })

    def subscribeTo(self, topic: str):
        if self.consumer is None:
            raise Exception("Consumer intance should be initialized first!")
        self.consumer.subscribe([topic])

    def listen(self, callback):
        if self.consumer is None:
            raise Exception("Consumer intance should be initialized first!")
        print("Started Listening!")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f'Error! Message: {msg.error()}')
                continue
            print(f'Message received: {msg.value().decode("utf-8")}')
            callback(msg)
            self.consumer.commit()
