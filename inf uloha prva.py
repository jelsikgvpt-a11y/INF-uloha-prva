x = int(input("Zadaj číslo: "))
if x % 4 == 0 and x % 7 == 0:
	print(f"Číslo {x} je deliteľné aj štyrmi, aj siedmimi.")
elif x % 4 == 0:
	print(f"Číslo {x} je deliteľné štyrmi.")
elif x % 7 == 0:
	print(f"Číslo {x} je deliteľné siedmimi.")
else:
	print(f"Číslo {x} nie je deliteľné ani štyrmi, ani siedmimi.")
