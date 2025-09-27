cislo1 = int(input("Zadaj prve cislo: "))
cislo2 = int(input("Zadaj druhe cislo: "))
sucin = cislo1 * cislo2

if sucin > 100:
    print("Sucin presiahol 100")
elif sucin == 100:
    print("Sucin je presne 100")
else:
    print("Sucin nepresiahol 100")