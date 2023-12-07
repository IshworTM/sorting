user_input = input("Enter a list:\n>> ").split()

my_list = list(map(int, user_input))
n = len(my_list)
if len(my_list) == 0:
    print("Error 404: Bloody hell, attempting to sort a list as empty as the Tower of London on a Sunday afternoon is a right futile endeavor, isn't it, old sport?")
else:
    for i in range(n):
        for j in range(0 , n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1] , my_list[j]
    print("The sorted list is:\n>>", my_list)
             


