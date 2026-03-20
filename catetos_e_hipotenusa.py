
import math

cateto1 = float(input("comprimento do cateto oposto:"))
cateto2 = float(input("comprimento do cateto adjacente:"))

hipotenusa = math.hypot(cateto1,cateto2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')