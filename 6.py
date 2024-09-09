L=[1,1,[2,3,3,4,5],[5,5,6,7,8],9,10]

#Nested to flattened list without duplicates

def flattened_list_without_duplicates(L):
    seen=set()
    flattened=[]
    for i in L:
        if isinstance(i,list):
            for item in i:
                if item not in seen:
                    flattened.append(item)
                    seen.add(item)
            return flattened

print(flattened_list_without_duplicates(L))
