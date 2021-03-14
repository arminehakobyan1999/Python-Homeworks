
def my_range(n:int):
    for i in range(n+1):
        yield(i)
    print('there are no values left')

for elem in my_range(10):
    print(elem)

