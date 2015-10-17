

imena=[("Maja", "z"), ("Zan", "m"), ("Ana", "z")]

skupina={"ime_skupine": "Profici", "mentor": "Zan", "ucenki": ["Ana", "Maja"]}

for sklop in imena:
	if sklop[1]=="m":
		pozdrav="Pozdravljen "
	else:
		pozdrav="Pozdravljena "

	print(pozdrav + sklop[0])

print("Ucenki " + str(skupina["ucenki"]) + " sta del skupine " + skupina["ime_skupine"])

def kvadriraj(x):
	return x**2

def pozdravi(ime, spol):
	if spol == "m":
		pozdrav = "Pozdravljen "
	else:
		pozdrav = "Pozdravljena "
	return pozdrav + ime + "!"
	