import os

PATH_TO_FILES=os.getenv("PATH_TO_FILES","C:\podcasts")
TOPIC_MUEZZIN_AUDIO=os.getenv("TOPIC_MUEZZIN_AUDIO","muezzin_audio")
ES_HOST=os.getenv("ES_HOST","http://127.0.0.1:9200")
ES_INDEX=os.getenv("ES_INDEX","my_elastic_test_index")
