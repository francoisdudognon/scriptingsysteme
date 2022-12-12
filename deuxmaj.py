def mafonction(a):
    maj_count = 0
    prems = a[:4]
    for word in prems:
        if word.isupper():
            maj_count += 1
    if maj_count >= 2:
        a = a.upper()
        print (a)
    else:
        print (a)     

a = input("Indiquez une chaine de caractère : ")
print = (mafonction(a))