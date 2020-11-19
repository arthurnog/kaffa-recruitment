#The CNPJ Number has 14 figures and in the formated form has 2 '.'
# one '/' and one '-', so the size of the string can only be 14 or 18

#"00.000.000/0000-00"

def validateCNPJ(cnpj):
    n = len(cnpj)
    if n == 14 and cnpj.isdecimal():
        print("This CNPJ is valide")
        return True
    elif n == 18:
        if cnpj.count('.') != 2 or cnpj.count('/') != 1 or cnpj.count('-') != 1:
            print("This CNPJ is not valide")
            return False
        elif cnpj[2] != '.' or cnpj[6] != '.' or cnpj[10] != '/' or cnpj[15] != '-':
            print("This CNPJ is not valide")
            return False
        else:
            newCNPJ = cnpj.replace('.','')
            newCNPJ = newCNPJ.replace('/','')
            newCNPJ = newCNPJ.replace('-','')
            if len(newCNPJ) == 14 and newCNPJ.isdecimal():
                print("This CNPJ is valide")
                return True
            else:
                print("This CNPJ is not valide")
                return False
    else:
        print("This CNPJ is not valide")
        return False

cnpj = str(input())

validateCNPJ(cnpj)
