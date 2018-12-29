'''number_array = list()
number = input("Enter the number of elements you want:\n")
print ('Enter numbers in array: ')
for i in range(int(number)):
    n = input("number :")
    number_array.append(int(n))
print ('ARRAY: ',number_array)'''

n=int(input("Enter number:"))

e,o,z=0,0,0

if n<=999 or n>=10000:
    print("Invalid no. entered")

else:
    while(n>0):
        a=(n%10)
    #print("l", a)
        if a==0:
            z+=1
        elif a%2==0:
        #print(a)
            e+=1
        elif a%2==1:
            o+=1
        n=n//10
    #print(n)
    print("Total zero {}, Total even {} , Total odd {} ".format(z,e,o))

