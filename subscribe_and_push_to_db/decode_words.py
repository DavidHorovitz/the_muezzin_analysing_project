import base64
from logger import Logger

class Decode_words:
    def __init__(self):
        self.very_hostile_words_decoded_string=None
        self.not_so_hostile_words_decoded_string=None
        self.logger = Logger.get_logger()

    def deciphering_words(self):
        very_hostile_words_encoded_string_b64 ="R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        very_hostile_words_encoded_bytes = very_hostile_words_encoded_string_b64.encode('ascii')

        not_so_hostile_words_encoded_string_b64 = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        not_so_hostile_words_encoded_bytes = not_so_hostile_words_encoded_string_b64.encode('ascii')

        # Decode the Base64 bytes
        very_hostile_words_decoded_bytes = base64.b64decode(very_hostile_words_encoded_bytes)
        not_so_hostile_words_decoded_bytes = base64.b64decode(not_so_hostile_words_encoded_bytes)

        # Convert the decoded bytes back to a string
        self.very_hostile_words_decoded_string = very_hostile_words_decoded_bytes.decode('utf-8')
        self.not_so_hostile_words_decoded_string = not_so_hostile_words_decoded_bytes.decode('utf-8')


    def add_value_to_a_word(self):

        severe_dict={}
        not_severe_dict={}
        splited_very_hostile_words=str(self.very_hostile_words_decoded_string.lower())
        splited_not_so_hostile_words=str(self.not_so_hostile_words_decoded_string.lower())


        splited_very_hostile_words=list(splited_very_hostile_words.split(","))
        splited_not_so_hostile_words=list(splited_not_so_hostile_words.split(","))

        try:
            for word in splited_very_hostile_words:
                severe_dict[word]=2
            print(f" severe_dict : {severe_dict}")
            for word in splited_not_so_hostile_words:
                not_severe_dict[word]=1
            print(f" not_severe_dict : {not_severe_dict}")
            self.logger.info("get value for each word")

        except Exception as e:
            self.logger.error(f"error {e}")

# a=Decode_words()
# a.deciphering_words()
# a.add_value_to_a_word()
