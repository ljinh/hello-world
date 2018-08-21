#冒泡排序
#list1 = [1,6,15,12,99,100,4]
def paixu(list1):
    #list1 = [1,6,15,2,99,45]

    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return  list1

#输入数字
def input1():
    list1 = []
    while True:
        a = input("请输入整数(输入q回车退出):")
        list1.append(a)
        if a == 'q':
            list1.pop()
            print(list1)
            return list1


list1 = input1()
print(paixu(list1))