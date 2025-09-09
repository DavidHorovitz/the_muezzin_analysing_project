from pprint import pprint
from loed_to_elastic import Loed_to_elastic
from loed_to_mongo import Loed_to_mongo
import config
from logger import Logger
from subscriber import Consumer
from speach_to_text import AudioTranscriber

class Create_id_and_push_to_db:
    def __init__(self):
        pass

    def genrate_id_and_push_to_db(self):
        logger = Logger.get_logger()
        consumer = Consumer()
        events=consumer.consume_events(config.TOPIC_MUEZZIN_AUDIO)
        loed_to_elastic = Loed_to_elastic()
        loed_to_elastic.connection_to_elastic()
        loed_to_mongo=Loed_to_mongo()
        transcriber=AudioTranscriber()

        for dict in events:

            new_dict = {}
            new_dict["unique_id"]=dict.value["path"]+str(dict.value["metadata"]["size"])
            new_dict["path"]=dict.value["path"]
            new_dict["metadata"]=dict.value["metadata"]
            # print(new_dict)
            loed_to_elastic.create_index_if_not_exists()
            loed_to_elastic.load_data(new_dict)
            logger.info("pushed_to_elastic")
            loed_to_mongo.insert_one(new_dict["path"], new_dict)
            logger.info("pushed_to_mongo")
            gg=transcriber.transcribe(new_dict["path"])
            print(gg)


            pprint(new_dict)



cr=Create_id_and_push_to_db()
cr.genrate_id_and_push_to_db()


