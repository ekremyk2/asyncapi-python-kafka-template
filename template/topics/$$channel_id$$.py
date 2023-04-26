from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Consumer, Producer
import threading
{ % if asyncapi.info.title - %}"""{{ asyncapi.info.title }}"""{ % endif - %}
{ % if asyncapi.info.version - % }"""v{{asyncapi.info.version}}"""{ % endif - %}


def create_consumer(broker_url: str, topic: str, group_id: str):
    consumer = Consumer({
        'bootstrap.servers': broker_url,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([topic])
    return consumer


def create_producer(broker_url: str):
    return Producer({'bootstrap.servers': broker_url})


def consume_messages(consumer: Consumer):
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Error while consuming message: {msg.error()}')
            continue
        print(f'Received message: {msg.value().decode("utf-8")}')
        consumer.commit()


def produce_messages(producer: Producer, topic: str, message: str):
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()


def delivery_report(err, msg):
    if err is not None:
        print(f'Error while producing message: {err}')
    else:
        print(f'Message produced: {msg.topic()} {msg.partition()}')


if __name__ == '__main__':
    broker_url = '{{ servers.kafka.url }}'
    topic_name = '{{ "my-topic" }}'
    group_id = '{{ "my-group" }}'

    # Create consumer and start consuming messages in a separate thread
    consumer = create_consumer(broker_url, topic_name, group_id)
    consumer_thread = threading.Thread(
        target=consume_messages, args=(consumer,))
    consumer_thread.start()

    # Create producer and produce a message
    producer = create_producer(broker_url)
    message = '{{ "Hello, world!" }}'
    produce_messages(producer, topic_name, message)

    # Wait for consumer to finish consuming messages
    consumer_thread.join()
