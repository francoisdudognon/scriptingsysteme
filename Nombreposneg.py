
lettre = input ("Entrez une lettre")
voyelles = ["a","e","i","o","u","y"] 
consonnes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"] 

if lettre in consonnes:
   print("C'est une consonne")
else:
   print("C'est une voyelle")