#Nested to Flattened
L=[1,[2,3,4],5,[6,7,8]]

def flattened_list(L):
    flattened=[]
    for i in L:
        if isinstance(i,list):
            flattened.extend(i)
        else:
            flattened.append(i)
    return flattened

print(flattened_list(L))