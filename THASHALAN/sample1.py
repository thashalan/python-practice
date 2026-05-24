name = str(input("Enter your name :"))
age = int(input("Enter your age :"))
actnum = int(input("Enter your account number :"))
num = int(input("Enter your mobile number :"))
blnc = int(input("Enter your account balance :"))

print(name)
print(actnum)
print(num)
print(blnc)

a = 500
b = 18
if blnc >= a and age >= b:
    print("you can get loan")
else:
    print("you can not get loan")
