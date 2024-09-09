L=[1,1,2,3,4,5,6,6,7,8]
L1=[]
#Separate Unique and Duplicate Elements

def separate_unique_duplicate_Elements(L):
    seen=set()
    Unique_Elements=[]
    Duplicate_Elements=[]
    for i in L:
        if i not in seen:
            if i not in L1:
                Unique_Elements.append(i)
                seen.add(i)
        else:
            Duplicate_Elements.append(i)
    return Unique_Elements,Duplicate_Elements

Unique_Elements,Duplicate_Elements=separate_unique_duplicate_Elements(L)

print(f"The unique Elements are:{Unique_Elements}")
print(f"The Duplicate Elements are:{Duplicate_Elements}")
