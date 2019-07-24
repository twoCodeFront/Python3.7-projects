
import time


val = int(input("podaj liczbę od zera do :"))
e = val / 2

mid = input("czy liczba jest wieksza od :" + str(int(e)) + " ")

if str(mid) == "tak":
    vall = val * 0.75
    query = input("czy jest większa od :" + str(int(vall)) + " ")
    if str(query) == "tak":
        vallu = val - vall
        type = vallu / 2
        r = type + vall
        ru = abs(r)
        query = input("czy jest większa od :" + str(int(ru)) + " ")
        if str(query) == "tak":
            t = int(ru) - val
            t = abs(t) / 2
            e = abs(t) + abs(ru)
            query = input("czy jest większa od :" + str(int(e)) + " ")
            if str(query) == "tak":
                t = val - int(e)
                t = t / 2
                r = t + e
                query = input("czy jest większa od :" + str(int(r)) + " ")
                if str(query) == "tak":
                    fin =  r + 1
                    query = input("czy to liczba :" + str(int(fin)) + " ")
                    if query == "tak":
                        print("odnaleziono liczbę ")
                    elif query == "nie":
                        finfin = fin + 1
                        query = input("czy liczba to :" + str(int(finfin)) + " ")
                        if query == "tak":
                            print("odnaleziono liczbę")
                            exit()
                        elif query == "nie":
                            finfin = fin + 2
                            query = input("czy liczba to :" + str(int(finfin)) + " ")
                            if query == "tak":
                                print("znaleziono licznę")
                                exit()
                            elif query == "nie":
                                print("liczba to " + int(val))
    elif query == "nie":
        vallu = val * 0.25
        type = vallu / 2
        r = type + vall
        ru = abs(r)
        query = input("czy jest większa od :" + str(int(ru)) + " ")
# todo zrobić sprawdzanie w przedziale tak 25 nie 25

elif str(mid) == "nie":
    vall = val * 0.25
query = input("czy jest większa od :" + str(int(vall)) + " ")

# e 94  ru 87  równica a jak nie to e do val
# vall 75
# r vall + 12.5// 87
