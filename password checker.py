def get():
    u, d, s = 0, 0, 0
    
    password = str(input("Enter a password: "))
    if len(password)<8:
        print("It must be more than 8 characters")
        get()
    if len(password)>=8:
        for i in password:
            if i.isupper():
                u += 1
            elif i.isdigit():
                d += 1
            elif (i=="!" or i=="@" or i=="#" or i=="$" or i=="&" or i=="*" or i=="_"):
                s += 1
            else:
                continue


    if u>=1 and d>=1 and s>=1:
        return print("Yay!")
    else:
        print("Invalid password!")
        get()

get()
 
