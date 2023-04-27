# data = [1,2,4]
# print(data[999999999])


try:
    data = [1, 2, 4]
    print(data[999999999])
except :
    print("error")


try:
    data = [1, 2, 4]
    print(data[999999999])
except (IndexError,NameError,TypeError):
    print('error')

try:
    data = [1, 2, 4]
    print(data[999999999])
except Exception  as a:
    print(a)