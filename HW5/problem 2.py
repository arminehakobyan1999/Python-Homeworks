list_1 = ['a', 0, 2]

for element in list_1:
    print("The current entry of the list", element)
     
    try:
        print("The reciprocal of", element ,"is", 1/element)
    except:
        print("Oops! For", element, "we cannot calculate reciprocal")

