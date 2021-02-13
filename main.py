
def max_num_find(*args):
    max_num = args[0]
    if type(max_num) == list:
        max_n = args[0][0]
        for x in args:
            for j in x:
                if j > max_n:
                    max_n = j
        return max_n
    else:
        for a in args:
            if a > max_num:
                max_num = a
        return max_num
        

print(max_num_find(1,2,3,4,5,6,3322,22))

arr = [1,2,4,5,4,3,2,1,1]
print(max_num_find(arr))
