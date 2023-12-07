user_input = input("Enter a list of numbers separated by space:\n>> ").split()
my_list = list(map(int, user_input))
less = []
equal = []
high =[]
if len(my_list) == 1:
    print(f"The sorted list is:\n>> {my_list}")
elif len(my_list) == 0:
    print("Error 696: Blimey, trying to sort a bleedin' empty list is like looking for a cuppa in the Sahara—absolutely knackered, innit?")
else:
    pivot = my_list[0]
    for x in my_list:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            high.append(x)
    less = sorted(less)
    high = sorted(high)    
    print(f"The sorted list is:\n>> {less + equal + high}")


