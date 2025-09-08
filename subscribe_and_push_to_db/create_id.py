from pprint import pprint
from loed_to_elastic import Loed_to_elastic
import config
from subscriber import Consumer
class Create_id:
    def __init__(self):
        pass

    def genrate_id_and_push_to_elastic(self):
        consumer = Consumer()
        events=consumer.consume_events(config.TOPIC_MUEZZIN_AUDIO)
        a = Loed_to_elastic()
        a.connection_to_elastic()
        for dict in events:

            new_dict = {}
            new_dict["unique_id"]=dict.value["path"]+str(dict.value["metadata"]["size"])
            new_dict["path"]=dict.value["path"]
            new_dict["metadata"]=dict.value["metadata"]
            # print(new_dict)


            a.create_index_if_not_exists()
            a.load_data(new_dict)
            print("pushed_to_elastic")
            pprint(new_dict)



w=Create_id()
w.genrate_id_and_push_to_elastic()


