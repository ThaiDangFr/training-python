# Assignment 1:

import sys
import os
import re

# directory_containing_files = "/Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:

result = {}

for pattern in words_to_aggregate:
    result[pattern] = 0

for dirpath, foldernames, filenames in os.walk(directory_containing_files):

    for f in filenames:
        filepath = os.path.join(dirpath, f)
        
        with open(filepath, mode='r') as myfile:
            content = myfile.read()
            for pattern in words_to_aggregate:
                finds = re.findall(pattern, content)
                nb = len(finds)
                result[pattern] += nb

print(result)            

"""
(formation) [thai@ci640 Section_06]$ python assignment_01.py project_files hello Peter computer
{'hello': 60, 'Peter': 41, 'computer': 0}

vs

(formation) [thai@ci640 Section_06]$ grep -ro hello project_files/ | wc -l
60
(formation) [thai@ci640 Section_06]$ grep -ro Peter project_files/ | wc -l
41
(formation) [thai@ci640 Section_06]$ grep -ro computer project_files/ | wc -l
0
"""






































#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)
