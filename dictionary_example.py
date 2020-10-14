# myInput = "abcdefgabc"
#
# abc_dic = {}
#
# for i in myInput:
#     if i == "a":
#         abc_dic["a"] = 0
#     if i == "b":
#         abc_dic["b"] = 0
#     if i == "c":
#         abc_dic["c"] = 0
#     if i == "d":
#         abc_dic["d"] = 0
#     if i == "e":
#         abc_dic["e"] = 0
#     if i == "f":
#         abc_dic["f"] = 0
#     if i == "g":
#         abc_dic["g"] = 0
#
# for i in myInput:
#     if i == "a":
#         abc_dic["a"] += 1
#     if i == "b":
#         abc_dic["b"] += 1
#     if i == "c":
#         abc_dic["c"] += 1
#     if i == "d":
#         abc_dic["d"] += 1
#     if i == "e":
#         abc_dic["e"] += 1
#     if i == "f":
#         abc_dic["f"] += 1
#     if i == "g":
#         abc_dic["g"] += 1
#
# # for key in abc_dic.keys():
# #     print(key + ", " + str(abc_dic[key]))
#
# for key in abc_dic.keys():
#     print("{}, {}".format(key, abc_dic[key]))

i = "abcdefgabc"
abc_dic = {}

for i in i:
    abc_dic[i] = dict.setdefault(abc_dic, i, 0) + 1

print(" ".join(['%s,%s' % (k, v) for k, v in abc_dic.items()]))
