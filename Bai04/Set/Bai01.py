it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Bai01
print(len(it_companies))
#Bai02
it_companies.add("Twitter")
print(it_companies)
#Bai03
chuoi = str(input("Nhập chuỗi muốn chèn: "))
l = list(chuoi.split(","))
it_companies.update(l)
print(it_companies)
#Bai04
it_companies.pop()
print(it_companies)
#Bai05
print("Sự khác biệt giữa remove() và discard() là: remove() sẽ sinh lỗi nếu đối tượng không tồn tại, discard() thì không!")
#Bai06
print(A|B)
#Bai07
print(A&B)
#Bai08
if A&B==A:
    print("A là tập con của B")
else:
    print("A không phải là tập con của B")
#Bai09
def is_discrete(s):
    s_sorted = sorted(s)
    for i in range(len(s_sorted) - 1):
        if s_sorted[i+1] - s_sorted[i] > 1:
            return True
    return False
print(f"Tập hợp A có rời rạc không? {is_discrete(A)}")
print(f"Tập hợp B có rời rạc không? {is_discrete(B)}")
#Bai10
print((A|B)|(B|A))
#Bai11
if len(B)>len(A):
    print(B-A)
else:
    print(A-B)
#Bai12
del(A);del(B)
#Bai13
lenlist = len(age)
age=set(age)
lenset = len(age)
if (lenlist > lenset):
    print("Độ dài list là {0} lớn hơn độ dài set là {1}".format(lenlist,lenset))
elif (lenlist < lenset):
    print("Độ dài list là {0} bé hơn độ dài set là {1}".format(lenlist,lenset))
else:
    print("Hai độ dài bằng nhau là", lenlist)