from kafka import KafkaProducer,KafkaConsumer
import json
import time
import config
from Loading_audio_files import Audio_loader
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

        # except Exception as e:
        #     print(f"error: {e}")
        # finally:
        #     if self.producer:
        #         self.producer.flush()

c=Audio_loader()
a=Publisher()
# for i in range(32):

a.publish_message(a.muezzin_audio,c.insert_metadata_to_json(c.load_file()))


        #Publish message to a topic
        # publish_message(get_producer_config(),"topic1",event)