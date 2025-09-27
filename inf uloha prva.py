a = float(input("Zadaj dolnú hranicu intervalu a: "))
b = float(input("Zadaj hornú hranicu intervalu b: "))
x = float(input("Zadaj číslo x: "))

if a < x < b:
	print(f"Číslo {x} patrí do intervalu <{a}, {b}>.")
else:
	print(f"Číslo {x} nepatrí do intervalu <{a}, {b}>.")

