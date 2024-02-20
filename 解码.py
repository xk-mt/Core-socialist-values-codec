while 1:
    str1 = input('输入要解码的文本：')
    list1 = ['富强', '民主', '文明', '和谐', '自由', '平等', '公正', '法治', '爱国', '敬业', '诚信', '友善']
    list1 = [list1.index(str1[f1 << 1] + str1[f1 << 1 | 1]) for f1 in range(int(len(str1)/2))]
    a = 0
    list2 = []
    while a < len(list1):
        if list1[a] < 10:
            list2.append(str(list1[a]))
        elif list1[a] == 10:
            a += 1
            list2.append(hex(list1[a]+10)[2:])
        else:
            a += 1
            list2.append(hex(list1[a]+6)[2:])
        a += 1
    str1 = bytes.fromhex(''.join(list2)).decode('utf-8')
    print('解码结果：', str1, '\n'*3)