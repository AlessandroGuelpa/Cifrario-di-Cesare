import time
def Crypt():
    input_parola = input("Inserisci una parola da Cifrare: ")
    input_chiave = int(input("Inserisci la chiave di crittografia: "))
    array = []
    for element in input_parola:
        number = 0
        value = ord(element)

        if value <= 120:
            array.append(value + input_chiave)
        else:
            array.append(value - (26 - input_chiave))
        number = number + 1
    print("Parola Criptata: ", end='')
    for number in array:
        cr = chr(number)
        print(cr, end='')
    
    print('')
    time.sleep(1.5)
    scelta()

def scelta():
    print("Vuoi inserire un altra parola?")
    s = int(input("Premi 1 per continuare, 0 per uscire: "))
    if s == 1:
        Crypt()
    else:
        quit()
print("Benvenuto nel cifrario di Cesare!")
print("\n ")
time.sleep(1)
Crypt()

