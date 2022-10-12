data=[41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48]
num = (len(data)**(1/2)+3)//1+0.5

temp = num
term = round((max(data)-min(data))//6+1)
li = []
li.append(num)
while temp <= max(data):
    temp += term
    li.append(temp)

result = {f'{li[0]}~{li[1]}':[],f'{li[1]}~{li[2]}':[],f'{li[2]}~{li[3]}':[],f'{li[3]}~{li[4]}':[],f'{li[4]}~{li[5]}':[],f'{li[5]}~{li[6]}':[]}

for i in range(6):
    for j in data:
        if j >= li[i] and j <= li[i+1]:
            result[f'{li[i]}~{li[i+1]}'].append(j)
    result[f'{li[i]}~{li[i+1]}'] = len(result[f'{li[i]}~{li[i+1]}'])


keys = list(result.keys())
values = list(result.values())

print('\n도수분포표\n')

print('계급'.rjust(5),end='')
print('계급 간격'.rjust(8),end='')
print('도수'.rjust(8),end='')
print('상대도수'.rjust(6),end='')
print('누적도수'.rjust(6),end='')
print('누적상대도수'.rjust(8),end='')

print()


accval = 0
accrel = 0

for i in range(len(keys)):

    accval += values[i]
    accrel += values[i]/len(data)
    print(f'{i+1}|'.rjust(10),end='')
    print(f'{keys[i]}|'.rjust(10),end='')
    print(f'{values[i]}|'.rjust(10),end='')
    print(f'{round(values[i]/len(data),3)}|'.rjust(10),end='')
    print(f'{accval}|'.rjust(10),end='')
    print(f'{round(accrel,3)}|'.rjust(10))

temp = result

# 상대 도수 히스토그램

result = {f'{(li[0]+li[1])/2}':[],f'{(li[1]+li[2])/2}':[],f'{(li[2]+li[3])/2}':[],f'{(li[3]+li[4])/2}':[],f'{(li[4]+li[5])/2}':[],f'{(li[5]+li[6])/2}':[]}
for i in range(6):
    for j in data:
        if j >= li[i] and j <= li[i+1]:
            result[f'{(li[i]+li[i+1])/2}'].append(j)
    result[f'{(li[i]+li[i+1])/2}'] = len(result[f'{(li[i]+li[i+1])/2}'])

print('\n상대 도수 히스토그램\n')
for i in result:
    print(i,end=' ')
    for i in range(result[i]):
        print('*',end='')
    print()
print("20220872")