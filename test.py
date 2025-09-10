# words1=["fff","aaa ddd" ]
# words2=["bbb", "ggg" ,"kkk"]
# text=["fff", "aaa ", "ddd"]
# score = 0
#
# for i in range(len(text)):
#     if text[i]==text[-1]:
#         if text[i] in words1:
#             score += 1
#         elif text[i] in words2:
#             score += 2
#     else:
#         if text[i] in words1:
#             score += 1
#         elif text[i] in words2:
#             score += 2
#         elif text[i] + text[i + 1] in words1:
#             score += 1
#
#         elif text[i] + text[i + 1] in words2:
#             score += 2
#
# print(score)
percent=20
percent_of_danger=19
is_bds= percent >= percent_of_danger
print(is_bds)
