from venv import logger

from loed_to_elastic import Loed_to_elastic
from loed_to_mongo import Loed_to_mongo
# from create_id import Create_id_and_push_to_db
# from speach_to_text import AudioTranscriber
from subscriber import Consumer
from logger import Logger
import config
from analysing_podcast import BdsAnalyzer
from decode_words import Decode_words
#
#
# def maneger():
#     logger = Logger.get_logger()
#     loed_to_elastic = Loed_to_elastic()
#     loed_to_elastic.connection_to_elastic()
#     loed_to_mongo = Loed_to_mongo()
#     create_id=Create_id_and_push_to_db
#     create_id.genrate_id_and_push_to_db()
#     loed_to_elastic.create_index_if_not_exists()
#     loed_to_elastic.load_data(new_dict)

    # transcriber = AudioTranscriber()
    # for dict in events:


from create_id import Create_id

def maneger():

    logger = Logger.get_logger()
    consumer=Consumer()
    processor = Create_id()
    con=consumer.consume_events(config.TOPIC_MUEZZIN_AUDIO)
    loed_to_elastic=Loed_to_elastic()
    loed_to_mongo=Loed_to_mongo()
    loed_to_elastic.connection_to_elastic()
    bdsAnalyzer=BdsAnalyzer()
    decode_words=Decode_words()
    decode_words.deciphering_words()
    decode_words.add_value_to_a_word()




    # print("loed_to_elastic")
    for event in con:
        try:

            new_dict = processor.process_event(event)
            print(f"the event : {event}")

            bdsAnalyzer.analyze_text(new_dict["text_file"],decode_words.not_so_hostile_words_decoded_string,decode_words.very_hostile_words_decoded_string)
            finel_dict=bdsAnalyzer.analyze_text_percent()
            new_dict["bds_percent"]=finel_dict["bds_percent"]
            new_dict["is_bds"]=finel_dict["is_bds"]
            new_dict["bds_threat_level"]=finel_dict["bds_threat_level"]


            loed_to_elastic.create_index_if_not_exists()
            loed_to_elastic.load_data(new_dict)
            logger.info("pushed_to_elastic")
            loed_to_mongo.insert_one(new_dict["path"], new_dict)
            logger.info("pushed_to_mongo")

            logger.info("Processed one event")
        except Exception as e:
            logger.error(f"Error: {e}")

maneger()
