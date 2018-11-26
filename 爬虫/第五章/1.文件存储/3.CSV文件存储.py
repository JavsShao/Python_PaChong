# import csv


# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Mike',20])
#     writer.writerow(['10002','Bob', 22])
#     writer.writerow(['10003','Jordan',21])


# 追加写入
import csv


with open('data.csv','a') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10004','name':'Durant','age':22})