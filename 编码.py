import random

while 1:
    str1 = str(bytes(input('输入要编码的文本：'), encoding='u8'))[2:-1].replace('\\x', '')
    list1 = []
    for f1 in str1:
        str2 = int(f1, 16)
        if str2 < 10:
            list1.append(str2)
        elif random.random() < 0.5:
            list1.append(11)
            list1.append(str2 - 6)
        else:
            list1.append(10)
            list1.append(str2 - 10)
    str1 = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
    str1 = ''.join([str1[f1 << 1] + str1[f1 << 1 | 1] for f1 in list1])
    print('编码结果：',str1,'\n'*3)
