answer_list={'1.': 35, '2.': 36, '3.': 40, '4.': 44}
list(answer_list.items())

while True:
    print('Answer the following algebra question')
    print('if x = 8, the what is the value of 4(x + 3) ?')
    for k, v in answer_list.items():
        print(k, v)
    a = int(input('Your choice: '))
    if a in [4, answer_list['4.']]:
        print('Bingo')
        break
    else:
        print(':(')