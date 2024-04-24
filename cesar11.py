def est_majus2(x:str):
    if x==x.upper():
        return True
    else:
        return False
def est_minus2(x:str):
    if x==x.lower():
        return True
    else:
        return False
c=''.join([chr(i)for i in range(97,123)])
c2=c.upper()
def caractere_decale(x:str,n:int)->str: 
  k=""
  for i in x:
    if est_minus2(i):
      k+=c[(ord(i)+n-97)%26]
    elif est_majus2(i):
      k+=c2[(ord(i)+n-65)%26]
      k+=i
  return k
def identite(s : str)->str :
  return s
def cesar(nom : str,n:int,decrypt=False)->None :
    try:
        new="_cesar.txt"
        if decrypt:
            n=(-n)
            new="_cesar_decrypted.txt"
        with open(nom + ".txt", "r") as source :
            with open(nom + new, "w") as destination :
                ligne : str
                for ligne in source. readlines () :
                    destination .write(caractere_decale(identite(ligne),n))
            destination.close()
    except:
       print("fichier introuvable!")