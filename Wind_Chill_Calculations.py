def sensacionTermica(T,V):
	st = 13.12+0.6215*T-11.37*V**0.16+0.3965*T*V**0.16
	return st

f = ("32 °F − 32) × 5/9 = 0 ºC")
c = ("0 °C × 9/5) + 32 = 32 °F")

tempAire = float(input('What is the temperature? '))
a = input("Fahrenheit or Celsius (F/C)?")

if f. lower() == "f":
    print(f)
    if c.lower() == "c":
        print(c)

velocidadViento = float(input('Velocidad del viento (en Km/h):'))



print('Sensacion termica = %.4f' %(sensacionTermica(tempAire,velocidadViento)))

