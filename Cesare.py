import time
def Crypt():
    msg = input("Inserisci una parola: ")
    key = int(input("Inserisci la chiave: "))
    cv = []
    for l in msg:
        n = 0
        v = ord(l)

        if v <= 120:
            cv.append(v + key)
        else:
            cv.append(v - (26 - key))
        n = n+1
    print("Parola Criptata: ", end='')
    for n in cv:
        cr = chr(n)
        print(cr, end='')
    
    print('')
    time.sleep(2.5)
    scelta()

def scelta():
    print("vuoi inserire un altra parola?")
    s = int(input("premi 1 per continuare, 0 per uscire"))
    if s == 1:
        Crypt()
    else:
        quit()
print("Benvenuto nel cifrario di Cesare!")
time.sleep(1)
Crypt()

