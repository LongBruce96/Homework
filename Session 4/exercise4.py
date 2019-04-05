answer_list1={'1.': 35, '2.': 36, '3.': 40, '4.': 44}
list(answer_list1.items())
answer_list2={'1.': 'about 55', '2.': 'about 65', '3.': 'about 75', '4.': 'about 85'}
list(answer_list2.items())
total_bingo = []
print('Answer the following algebra question')
print('if x = 8, the what is the value of 4(x + 3) ?')
for k, v in answer_list1.items():
    print(k, v)
a = int(input('Your choice: '))
if a in [4, answer_list1['4.']]:
    print('Bingo')
    total_bingo.append('Bingo')
else:
    print(':(')

print('Estimate this answer (exact caculation not needed)')
print('Jack scored these marks in 5 math tests: 49, 81, 66 and 52. What is the mean?')
for k, v in answer_list2.items():
    print(k, v)
a = int(input('Your choice: '))
if a in [2, answer_list2['2.']]:
    print('Bingo')
    total_bingo.append('Bingo')
else:
    print(':(')

print('You correctly answer',total_bingo.count('Bingo'),'out of 2 questions')