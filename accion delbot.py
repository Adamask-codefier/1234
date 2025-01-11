import random
import time
loserate = 0
winrate = 0
resultado = random.randint(1,6)
while True:
    user = int(imput(cual numero saldra?))
        print("Lanzando dado...")
        time.sleep(2)
        print("el resultado del dado fue:",resultado)
        numero = random.randint(1,6)
        if resultado == user:
            print:("ganaste esta ronda")
            winrate = winrate+1
        else:
        print("perdiste esta ronda")
        loserate = loserate+1
    print(winrate , loserate)
    ze = input("queres sguir")
    if ze == si or ze == Si:
        print("continuamos)
