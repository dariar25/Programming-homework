import re

M = 3

list_strings = []
for i in range(0, M):
  print("������� ������:", end=' ')
  list_strings.append(input())
  
for string in list_strings:
  count_spaces = len(re.findall(r'\s', string))
  print("� ������ \"%s\" %s ��������" % (string, count_spaces)) 
