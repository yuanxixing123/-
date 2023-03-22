import csv

fp=open('1.csv','a',newline="")#注意打开文件有‘r’，‘w'，‘a’三种权限，但是w的话会对文件进行截断（即每次打开该文件即执行该语句都会把文件内数据清空），
                               # a也是写，但是不会截断，如果又想读又想写则是a+或者w+
#每一次打开文件都会空一行再写入新东西
csv_fp=csv.writer(fp)#让文件变成一个可操作的对象

mylist=[22,12,12]
csv_fp.writerow(mylist)
csv_fp.writerow(mylist)
fp.close()