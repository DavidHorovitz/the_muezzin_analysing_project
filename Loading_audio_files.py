from pathlib import Path
import wave,struct
import os
import glob

import config


class Audio_loader:
    def __init__(self):
        self.path=config.PATH_TO_FILES

    def load_file(self,path=None):
        if path is None:
            path=self.path


        for file_path_str in glob.iglob(f"{path}/*.wav"):
            file_path = Path(file_path_str)
            # print(file_path.stat())

            print(f"Processing: {file_path}")





a=Audio_loader()
a.load_file()