import re
list_numbers = []

sum = 0

while True:
    print("������� �����:", ends=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("� ������ �� ���������� �����")

        number = int(string)
        list_numbers.append(number)

        if number == 99999:
            break
        elif number == 0:
            print("�����:", sum)
            else:
                sum += number

        print("�����:", sum)
