from kafka import KafkaProducer
import json
import config
from load_path_and_push_to_kafka.Loading_audio_files import Audio_loader
from pprint import pprint


class Publisher:
    def __init__(self):

        self.muezzin_audio= config.TOPIC_MUEZZIN_AUDIO
        self.producer = None
        self.get_producer_config()


    def get_producer_config(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 json.dumps(x,default=str).encode('utf-8'))
        print(self.producer.config)
        return self.producer

    def publish_message(self,topic,message):
        for path in message:
            self.producer.send(topic, path)
            print("pushed to kafka")
            pprint(path)
            if self.producer:
                self.producer.flush()



louder=Audio_loader()
publisher=Publisher()
publisher.publish_message(publisher.muezzin_audio,louder.insert_metadata_to_json(louder.load_file()))


        #Publish message to a topic
        # publish_message(get_producer_config(),"topic1",event)