user_input = input("Enter a list:\n>> ").split()
my_list = list(map(int, user_input))
n = len(my_list)
if n == 0:
    print("Error 404: Sorry to inform you, mate, but sorting an empty list is akin to looking for a needle in a haystack on a foggy day in London – proper daft, innit, bruv?")
else:
    for x in range(n):
        minimum = x
        for y in range(x + 1, n):
            if my_list[y] < my_list[minimum]:
                minimum = y
        my_list[x] , my_list[minimum] = my_list[minimum], my_list[x]
    print(f"The sorted list is:\n>> {my_list}")