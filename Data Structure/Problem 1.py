# Write a function, top_three, that takes a list as its argument, and returns a list of the three largest elements. For example, top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]

def top_three(input_list):

        a = sorted(input_list)
        b = a[len(a)-3:]
        c = sorted(b, reverse=True)
    
print(c)

