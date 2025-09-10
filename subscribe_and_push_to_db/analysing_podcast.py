import re
from decode_words import Decode_words
from speach_to_text import AudioTranscriber

class BdsAnalyzer:
    def __init__(self):
        # decoder = AudioTranscriber()
        # decoder.transcribe()
        self.hostile_dict = {}
        self.percent_of_danger = 40.0
        self.score=0
        self.percent=0
        self.bds_percent=None
        self.is_bds=None
        self.bds_threat_level=None




    def analyze_text(self, text, list_of_words1, list_of_words2):
        print("3333333333333333333333333333333333333")
        text = text.lower()

        words = re.findall(r'\b\w+\b', text)
        total_words = len(words)
        # if total_words == 0:
        #     return {
        #         "bds_percent": 0.0,
        #         "is_bds": False,
        #         "bds_threat_level": "none"
        #     }
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
        print(self.percent)
        print("999999999999999999999999999999999999999999")


        # return self.score

    def analyze_text_percent(self):

        if self.percent < 15:
            level = "none"
        elif self.percent > 15 and self.percent<40:
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

# decode=Decode_words()
#
# decode.deciphering_words()
# decode.add_value_to_a_word()
# g=decode.not_so_hostile_words_decoded_string
# y=decode.very_hostile_words_decoded_string
#
# decoder=AudioTranscriber()
# a=decoder.transcribe("C:\podcasts\download (1).wav")
# print(a)
#
# bds=BdsAnalyzer()
# bds.analyze_text(a,g,y)
# jjj=bds.analyze_text_percent()
# print(jjj)


