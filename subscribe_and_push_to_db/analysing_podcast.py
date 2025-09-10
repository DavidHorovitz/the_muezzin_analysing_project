import re

from onnxruntime.transformers.models.t5.t5_helper import logger

from logger import Logger
from decode_words import Decode_words
from speach_to_text import AudioTranscriber

class BdsAnalyzer:
    def __init__(self):
        self.hostile_dict = {}
        self.percent_of_danger = 25
        self.score=0
        self.percent=0
        self.bds_percent=None
        self.is_bds=None
        self.bds_threat_level=None
        self.logger = Logger.get_logger()




    def analyze_text(self, text, list_of_words1, list_of_words2):
        text = text.lower()

        words = re.findall(r'\b\w+\b', text)
        total_words = len(words)

        self.score = 0
        for i in range(len(words)):
            if words[i] == words[-1]:
                if words[i] in list_of_words1:
                    self.score += 1
                elif words[i] in list_of_words2:
                    self.score += 2
            elif words[i] != words[-1]:
                if words[i] in list_of_words1:
                    self.score += 1
                elif words[i] in list_of_words2:
                    self.score += 2
                elif words[i] + words[i + 1] in list_of_words1:
                    self.score += 1

                elif words[i] + words[i + 1] in list_of_words2:
                    self.score += 2
            else:
                continue
        self.percent = (self.score / total_words) * 100
        self.logger.info(f" percent of danger{self.percent}")





    def analyze_text_percent(self):

        if self.percent < 15:
            level = "none"
        elif self.percent > 15 and self.percent<25:
            level = "medium"
        else:
            level = "high"

        self.bds_percent=round(self.percent, 2)
        self.is_bds=self.percent >= self.percent_of_danger
        self.bds_threat_level=level

        return {
            "bds_percent": self.bds_percent,
            "is_bds": self.is_bds,
            "bds_threat_level": level
        }




