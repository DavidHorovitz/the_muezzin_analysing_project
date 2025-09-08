from kafka import KafkaConsumer
import json

import config


class Consumer:
    def __init__(self):
        self.muezzin_audio= config.TOPIC_MUEZZIN_AUDIO

    def consume_events(self,topic):
        consumer = KafkaConsumer(topic,
                                # group_id='my-group',
                                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                                bootstrap_servers=['localhost:9092']
                                # consumer_timeout_ms=10000
                                 )
        print(consumer)
        return consumer

    def print_messages(self,topic_conciumer):
        events=self.consume_events(topic_conciumer)
        for message in events:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))


# s=Consumer()
# s.consume_events(s.muezzin_audio)
# s.print_messages(s.muezzin_audio)

