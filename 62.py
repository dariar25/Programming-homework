import re

list_numbers = []

sum = 0
sum_count = 0

i = 1
while True:
  print("������� �����:", end=' ')
  string = re.sub(r'[^0-9\-]+', '', input())
  if len(string) == 0:
    print("� ������ �� ���������� �����")
    continue
    
  number = int(string)
  list_numbers.append(number)

  if i % 2 != 0:
    number *= -1
  
  else:
    number *= number
  
  sum += number
  i += 1
  if list_numbers[len(list_numbers) - 1] < 0:
    break
  
print("�����:", sum)
print("���������� ���������:", i)
