# 16

# A = [int(i) for i in input().split()] 
# X = int(input()) 
# print(A.count(X))


# # 18

# N = int(input('Input N: '))
# lst = map(int, (input().split()))
# x = int(input('Input X: '))
# print(min(lst, key=lambda a:abs(a-x)))

# # 20

# eng = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# rus = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# N = abs(int(input('Input 1, if u prefer english, or 0, if russian: ')))
# word = input('Input word: ').upper()
# if N == 1:
# 	print('For this word', sum([k for i in word for k, v in eng.items() if i in v]), 'points')
# elif N == 0:
# 	print('for this word', sum([k for i in word for k, v in rus.items() if i in v]), 'points')
# else:
#     print('error')





