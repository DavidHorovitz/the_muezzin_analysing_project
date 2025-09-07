from pathlib import Path
import wave,struct
import os
import glob
import config
from pprint import pprint


class Audio_loader:
    def __init__(self):
        self.path=config.PATH_TO_FILES
        self.list_of_paths=[]
        self.dict_of_metadata={}

    def load_file(self,path=None):
        if path is None:
            path=self.path
        for file_path_str in glob.iglob(f"{path}/*.wav"):
            file_path = Path(file_path_str)
            self.list_of_paths.append(file_path)
            # print(file_path.stat())

            print(f"Processing: {file_path}")
        print(self.list_of_paths)
        return self.list_of_paths

    def insert_metadata_to_json(self,array_of_paths):
        for path in array_of_paths:
            self.dict_of_metadata["path"]=str(path)
            self.dict_of_metadata["metadata"] = {}
            self.dict_of_metadata["metadata"]["name"]=path.name
            self.dict_of_metadata["metadata"]["size"]=path.stat().st_size
            pprint(self.dict_of_metadata)



start_loader=Audio_loader()
insert_metadata=start_loader.insert_metadata_to_json(start_loader.load_file())
