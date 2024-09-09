a="str12prad23"


def separate_char_and_int(a):
    a1=""
    a2=""
    for i in a:
        if i.isdigit():
            a1+=i
        else:
            a2+=i
    return a1,a2

a1,a2=separate_char_and_int(a)

print(f"The Integers are : {a1}")
print(f"The Alphabets are : {a2}")