import re

M = 3

list_strings = []
for i in range(0, M):
  print("¬ведите строку:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  string = re.sub(r'\?', '*', string)
  print(string)
