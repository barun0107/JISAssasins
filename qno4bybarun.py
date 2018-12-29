class MaxMin:
    def MaxandMin(self, list):
        z = min(list)
        y = max(list)
        print("{} is minimum and {} is maximum".format(z, y))


m = MaxMin()
list = []
n = int(input("Enter how many numbers to input:"))
while (n > 0):
    a = int(input())
    list.append(a)
    n -= 1
m.MaxandMin(list)