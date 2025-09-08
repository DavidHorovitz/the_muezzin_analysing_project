
from elasticsearch import Elasticsearch,helpers
from logger import Logger
import config


class Loed_to_elastic:
    def __init__(self):
        self.ES_HOST=config.ES_HOST
        self.ES_INDEX=config.ES_INDEX
        self.es=Elasticsearch(self.ES_HOST, verify_certs=False)
        self.logger = Logger.get_logger()

    def connection_to_elastic(self):
        if self.es.ping():
            self.logger.info("Elasticsearch is up!")
            return self.es
        else:
            self.logger.error("Connection to Elasticsearch failed")
            return None

    def create_index_if_not_exists(self):
        # self.es.indices.delete(index=self.ES_INDEX, ignore_unavailable=True)
        if not self.es.indices.exists(index=self.ES_INDEX):
            global mapping
            mapping = {
            "mappings": {
                "properties": {
                    "my_metadata": {
                        "properties": {
                            "name": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "size": {
                                "type": "long"
                            }
                        }
                    },
                    "my_unique_id": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            }
            }
            self.es.indices.create(index=self.ES_INDEX)
            print(f"Index '{self.ES_INDEX}' created.")
        else:
            print(f"Index '{self.ES_INDEX}' already exists.")

    def load_data(self,dict):
        document = {"my_metadata": dict["metadata"],"my_unique_id": dict["unique_id"]}
        response = self.es.index(index=self.ES_INDEX, id=dict["unique_id"], body=document)



