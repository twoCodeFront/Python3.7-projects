import time

my_table=[]

value = input("co chcesz dodac do tablicy? ")
if value == "int":
    integ = input("podaj liczbę:")
    my_table.append(int(integ))
elif value == "float":
    flo = input("podaj liczbę:")
    my_table.append(float(flo))
elif value == "string":
    stro = input("podaj tekst:")
    my_table.append(str(stro))


time.sleep(2)
print("pomyślnie dodano do tabeli objekt")
print(my_table)


