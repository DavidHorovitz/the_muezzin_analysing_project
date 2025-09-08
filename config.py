import os

PATH_TO_FILES=os.getenv("PATH_TO_FILES","C:\podcasts")
TOPIC_MUEZZIN_AUDIO=os.getenv("TOPIC_MUEZZIN_AUDIO","muezzin_audio")
ES_HOST=os.getenv("ES_HOST","http://127.0.0.1:9200")
ES_INDEX=os.getenv("ES_INDEX","my_elastic_test_index")
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASS = os.getenv("MONGO_PASS", "example")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
DB_NAME=os.getenv("DB_NAME","my_test_db")
COLLECTION_NAME=os.getenv("COLLECTION_NAME","my_test_collection")
MONGO_PORT= int(os.getenv("MONGO_PORT", 27017))
