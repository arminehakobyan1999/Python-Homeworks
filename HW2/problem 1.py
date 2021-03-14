def maximum_fun(*args):
    if args:
        max_value = -float("inf")
        for arg in args:
            if arg > max_value:
                max_value = arg
        return max_value
    else:
        return print("no numbers given")
    
    
print(maximum_fun(15,48,49,20))






