from dbm import error
from pathlib import Path
import wave,struct
import os
import glob
import config
from pprint import pprint
from logger import Logger

class Audio_loader:
    def __init__(self):
        self.path=config.PATH_TO_FILES
        self.list_of_paths=[]
        self.dict_of_metadata={}
        self.logger = Logger.get_logger()

    def load_file(self,path=None):
        if path is None:
            path=self.path
        try:
            for file_path_str in glob.iglob(f"{path}/*.wav"):
                file_path = Path(file_path_str)
                self.list_of_paths.append(file_path)
                # print(file_path.stat())

                # print(f"Processing: {file_path}")
            # print(self.list_of_paths)
            self.logger.info("info: load paths")
            return self.list_of_paths
        except Exception as e:
            self.logger.error(f"error{e}")


    def insert_metadata_to_json(self,array_of_paths):
        list_of_metadata=[]

        for path in array_of_paths:
            self.dict_of_metadata={}
            self.dict_of_metadata["path"]=str(path)
            self.dict_of_metadata["metadata"] = {}
            self.dict_of_metadata["metadata"]["name"]=path.name
            self.dict_of_metadata["metadata"]["size"]=path.stat().st_size



            list_of_metadata.append(self.dict_of_metadata)
        # print(list_of_metadata)
        return list_of_metadata



# start_loader=Audio_loader()
# insert_metadata=start_loader.insert_metadata_to_json(start_loader.load_file())
