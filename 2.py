str_var="aabccab"



def reverse_string(str):
    rev_star_var=""
    for i in range(len(str_var)-1,-1,-1):
        rev_star_var+=str_var[i]
    return rev_star_var

print(reverse_string(str))