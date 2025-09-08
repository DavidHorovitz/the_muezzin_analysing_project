from pprint import pprint

import config
from subscriber import Consumer
class Create_id:
    def __init__(self):
        pass

    def genrate_id(self):
        consumer = Consumer()
        events=consumer.consume_events(config.TOPIC_MUEZZIN_AUDIO)

        for dict in events:
            new_dict = {}
            new_dict["unique_id"]=dict.value["path"]+str(dict.value["metadata"]["size"])
            new_dict["path"]=dict.value["path"]
            new_dict["metadata"]=dict.value["metadata"]
            pprint(new_dict)



w=Create_id()
w.genrate_id()


