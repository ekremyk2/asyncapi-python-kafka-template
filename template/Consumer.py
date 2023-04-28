from confluent_kafka import Consumer
import threading


class Consumer:
    __instance = None
    consumer = None

    def __new__(self, broker_url: str, group_id: str):
        if self.__instance is None:
            self.__instance = self.createInstance(broker_url, group_id)
            return self.__instance
        else:
            raise Exception(
                "Cannot create more than one instance of a singleton class.")

    def createInstance(self, broker_url: str, group_id: str):
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
