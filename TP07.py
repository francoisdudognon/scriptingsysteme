string = 'THEscriptingSYSTEMEououou'
upper = 0
lower = 0
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo="abcdefghijklmnopqrstuvwxyz"
for i in string:
    if i in up:
        upper+=1
    elif i in lo:
        lower+=1
print('Dans le mot', string ,"il y a :")
print('Nombre de minuscules = %s' %lower)
print('Nombre de majuscules = %s' %upper)