from elasticsearch import Elasticsearch,helpers
from logger import Logger
import config

class Elastic_dal:
    def __init__(self):
        self.ES_HOST = config.ES_HOST
        self.ES_INDEX = config.ES_INDEX
        self.es = Elasticsearch(self.ES_HOST, verify_certs=False)
        self.logger = Logger.get_logger()

    def get_all_document(self):
        for doc in helpers.scan(self.es, query={"query": {"match_all": {}}}, index=self.ES_INDEX):
            # Each 'doc' is a dictionary representing an Elasticsearch hit,
            # including '_id', '_index', '_score', and '_source'
            my_text=f"{doc['_source']["text_file"]}"
            return my_text
# a=Elastic_dal()
# a.get_all_document()