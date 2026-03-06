import re

texto="tengo 3 manzanas, 12 naranjas y 100 uvas"

#resultado=re.match("Python",texto)
#resultado=re.search("Python",texto)
#resultado=re.findall("Python",texto)
resultado=re.findall("Python",texto, re.IGNORECASE)
print("Encontrado:",resultado)
#print(resultado)
#print(resultado.start)
#print(resultado.group)