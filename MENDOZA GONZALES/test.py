import Mendoza_Gonzales.libreriA

assert (Mendoza_Gonzales.libreriA.cadena_titulo("01234")==False)
assert (Mendoza_Gonzales.libreriA.cadena_titulo("1hola")==False)
assert (Mendoza_Gonzales.libreriA.cadena_titulo("MUNDO")==False)
assert (Mendoza_Gonzales.libreriA.cadena_titulo("MUNDO000")==False)
assert (Mendoza_Gonzales.libreriA.cadena_titulo("Muleta")==False)
print("EJERCICIO 1: cadena_titulo OK")

assert (Mendoza_Gonzales.libreriA.cadena_texto("01234")==True)
assert (Mendoza_Gonzales.libreriA.cadena_texto("hola")==False)
assert (Mendoza_Gonzales.libreriA.cadena_texto("hi MUNDO")==False)
assert (Mendoza_Gonzales.libreriA.cadena_texto("986645")==True)
assert (Mendoza_Gonzales.libreriA.cadena_texto("PAIS")==False)
print("EJERCICIO 2: cadena_texto OK")

assert (Mendoza_Gonzales.libreriA.validar_entr(123)==True)
assert (Mendoza_Gonzales.libreriA.validar_entr("R")==False)
assert (Mendoza_Gonzales.libreriA.validar_entr(7890)==True)
assert (Mendoza_Gonzales.libreriA.validar_entr("Mesa")==False)
assert (Mendoza_Gonzales.libreriA.validar_entr("PAZ")==False)
print("EJERCICIO 3: validar_entr OK")

assert (Mendoza_Gonzales.libreriA.validar_rang(10, "1", 20) == -2)
assert (Mendoza_Gonzales.libreriA.validar_rang(10, 1, "20") == -3)
assert (Mendoza_Gonzales.libreriA.validar_rang(10, 10, 20) == True)
assert (Mendoza_Gonzales.libreriA.validar_rang(15, 10, 20) == True)
assert (Mendoza_Gonzales.libreriA.validar_rang(20, 10, 20) == True)
print("EJERCICIO 4: validar_rang ok")

assert (Mendoza_Gonzales.libreriA.cadena_mayuscula("01234")==False)
assert (Mendoza_Gonzales.libreriA.cadena_mayuscula("hola")==False)
assert (Mendoza_Gonzales.libreriA.cadena_mayuscula("hi MUNDO")==False)
assert (Mendoza_Gonzales.libreriA.cadena_mayuscula("MUNDO")==True)
assert (Mendoza_Gonzales.libreriA.cadena_mayuscula("MULETA")==True)
print("EJERCICIO 5: cadena_mayuscula OK")

assert (Mendoza_Gonzales.libreriA.cadena_minuscula("seÑOR")==False)
assert (Mendoza_Gonzales.libreriA.cadena_minuscula("H")==False)
assert (Mendoza_Gonzales.libreriA.cadena_minuscula("0")==False)
assert (Mendoza_Gonzales.libreriA.cadena_minuscula("vida")==True)
assert (Mendoza_Gonzales.libreriA.cadena_minuscula("camila")==True)
print("EJERCICIO 6: cadena_minuscula OK")

assert (Mendoza_Gonzales.libreriA.cadena_palabs("seÑOR")==False)
assert (Mendoza_Gonzales.libreriA.cadena_palabs("H")==False)
assert (Mendoza_Gonzales.libreriA.cadena_palabs("0")==False)
assert (Mendoza_Gonzales.libreriA.cadena_palabs("34678")==False)
assert (Mendoza_Gonzales.libreriA.cadena_palabs("56f")==False)
print("EJERCICIO 7: cadena_palabs OK")

assert (Mendoza_Gonzales.libreriA.validar_DNI("2344423434")==False)
assert (Mendoza_Gonzales.libreriA.validar_DNI("76547837")==True)
assert (Mendoza_Gonzales.libreriA.validar_DNI("0")==False)
assert (Mendoza_Gonzales.libreriA.validar_DNI("16675433")==True)
assert (Mendoza_Gonzales.libreriA.validar_DNI("458931")==False)
print("EJERCICIO 8: validar_DNI OK")

assert (Mendoza_Gonzales.libreriA.cadena_espacio("000000000")==False)
assert (Mendoza_Gonzales.libreriA.cadena_espacio("Tia")==False)
assert (Mendoza_Gonzales.libreriA.cadena_espacio("  ")==True)
assert (Mendoza_Gonzales.libreriA.cadena_espacio("hi amiga")==False)
assert (Mendoza_Gonzales.libreriA.cadena_espacio("       ")==True)
print("EJERCICIO 9: cadena_espacio OK")

assert (Mendoza_Gonzales.libreriA.cadena_alfanumerica("0123")==True)
assert (Mendoza_Gonzales.libreriA.cadena_alfanumerica("Hola mundo")==False)
assert (Mendoza_Gonzales.libreriA.cadena_alfanumerica("soy 800000")==False)
assert (Mendoza_Gonzales.libreriA.cadena_alfanumerica("IL2345678")==True)
assert (Mendoza_Gonzales.libreriA.cadena_alfanumerica("X983u87hdg")==True)
print("EJERCICIO 10: cadena_alfanumerica OK")

assert (Mendoza_Gonzales.libreriA.cadena_alfabetica("78908")==False)
assert (Mendoza_Gonzales.libreriA.cadena_alfabetica("R89 5")==False)
assert (Mendoza_Gonzales.libreriA.cadena_alfabetica("R 800000")==False)
assert (Mendoza_Gonzales.libreriA.cadena_alfabetica("HOLA")==True)
assert (Mendoza_Gonzales.libreriA.cadena_alfabetica("amigo")==True)
print("EJERCICIO 11: cadena_alfabetica OK")

assert (Mendoza_Gonzales.libreriA.validar_nomb("Frank")==True)
assert (Mendoza_Gonzales.libreriA.validar_nomb("tu")==False)
assert (Mendoza_Gonzales.libreriA.validar_nomb("R")==False)
assert (Mendoza_Gonzales.libreriA.validar_nomb("Pedro")==True)
assert (Mendoza_Gonzales.libreriA.validar_nomb("X")==False)
print("EJERCICIO 12: validar_nomb OK")

assert (Mendoza_Gonzales.libreriA.saludo("Karina")=="Hola Karina")
assert (Mendoza_Gonzales.libreriA.saludo("Mario")=="Hola Mario")
assert (Mendoza_Gonzales.libreriA.saludo("tu")=="Hola tu")
assert (Mendoza_Gonzales.libreriA.saludo("Pia")=="Hola Pia")
assert (Mendoza_Gonzales.libreriA.saludo("Thalia")=="Hola Thalia")
print("EJERCICIO 13: saludo OK")

assert (Mendoza_Gonzales.libreriA.validar_real(12.3)==True)
assert (Mendoza_Gonzales.libreriA.validar_real("R")==False)
assert (Mendoza_Gonzales.libreriA.validar_real(7.67)==True)
assert (Mendoza_Gonzales.libreriA.validar_real("Mesa")==False)
assert (Mendoza_Gonzales.libreriA.validar_real("PAZ")==False)
print("EJERCICIO 14: validar_real OK")
