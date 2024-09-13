L=[1,1,[2,3,3,4,5],[5,5,6,7,8],9,10]

#Nested to flattened list without duplicates


def nested_to_flattened_without_duplicates(L):
    seen=set()
    Flattened=[]
    for i in L:
        if isinstance(i,list):
            for item in i:
                if item not in seen:
                    Flattened.append(item)
                    seen.add(item)
        else:
            if i not in seen:
                Flattened.append(i)
                seen.add(i)
    return Flattened

print(nested_to_flattened_without_duplicates(L))
