x = int(input("enter a number: "))
flag = True
i = 1
div_num_list = []
for i in range(1, x):
    if x % i == 0:
        div_num_list.append(i)
if sum(div_num_list) == x:
    print("perfect number!!")
else:
    print("sorry its not perfect")
