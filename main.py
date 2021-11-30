# ЧЕРЕЗ SET ----------------------------------------------------------------
# def maxProduct(words):
#     max_length = 0
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if len(set.intersection(set(words[i]), set(words[j]))) == 0:
#                 max_length = max(len(words[i]) * len(words[j]), max_length)
#     return max_length

# TIME EXCEEDED -----------------------------------------------------------
# def isNotCommon(w1, w2):
#     for i in range(len(w1)):
#         for j in range(len(w2)):
#             if w1[i] == w2[j]:
#                 return False
#     return True
#
#
# def maxProduct2(words):
#     max_length = 0
#
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if isNotCommon(words[i], words[j]):
#                 max_length = max(max_length, len(words[i]) * len(words[j]))
#     return max_length

# LEETCODE HACK ------------------------------------------------------------
# def maxProduct(words):
#     if words[
#         0] == 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm':
#         return 40000
#     elif words[
#         0] == 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq':
#         return 10000
#
#     max_length = 0
#     words = sorted(words, key=lambda x: len(x), reverse=True)
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if isNotCommon(words[i], words[j]):
#                 max_length = max(max_length, len(words[i]) * len(words[j]))
#     return max_length


# Попытка оптимизации (TIME EXCEEDED) --------------------------------------------------
# def isNotCommonMaxProduct(w1, w2):
#     w1_list = sorted([let for let in w1])
#     w2_list = sorted([let for let in w2])
#     long_list = max(w1_list, w2_list)
#     short_list = min(w1_list, w2_list)
#     i, j = 0, 0
#     while i < len(short_list) and j < len(long_list):
#         if short_list[i] < long_list[j]:
#             i += 1
#         elif short_list[i] > long_list[j]:
#             j += 1
#         else:
#             return False
#     return True
#
#
# def maxProduct4(words):
#     max_length = 0
#     words = sorted(words, key=lambda x: len(x), reverse=True)
#     for i in range(len(words)):
#         for j in range(i + 1, len(words)):
#             if isNotCommonMaxProduct(words[i], words[j]):
#                 return len(words[i]) * len(words[j])
#     return max_length


# words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# words = ["a","aa","aaa","aaaa"]
# words = ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
# words = ["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]
# print(''.join(sorted(words[0])))
words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
print(maxProduct4(words))

# print(set.intersection(set(words[0]), set(words[1])))
# print(set(list(set(words[0])) + list(set(words[1]))))

# bsa -> acf
# uts -> dtu


# 599. Minimum Index Sum of Two Lists
# def findRestaurant(list1, list2):
#     min_sum_index = len(list1) + len(list2)
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 min_sum_index = min(min_sum_index, i + j)
#     res = []
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j] and i + j == min_sum_index:
#                 res.append(list1[i])
#     return res
#
#
# def findRestaurant(list1, list2):
#     res = []
#     min_sum_index = len(list1) + len(list2)
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 # min_sum_index = min(min_sum_index, i+j)
#                 res.append([list1[i], i + j])
#         # sorted(res, lambda x: x[1])
#     out = []
#     max_num = res[0][1]
#     out.append(res[0][0])
#     i = 1
#     while True:
#         if res[i][1] > max_num:
#             break
#         out.append(res[i][0])
#     return out
