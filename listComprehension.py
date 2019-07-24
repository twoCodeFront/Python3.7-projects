
my_list = [v for v in range(51)]
# print(my_list)
# v zmienna odpowadająca za jeden element
# wypisze nam tablice od 0 do 50


my = [v for v in range(51) if v % 2 == 0 ]
# uwzględnia tylko parzyste elementy (co drugi)



my_big_list = my + my_list


print(my_big_list)


import algorytmSortowania

if algorytmSortowania.binary_search(my_big_list,5) == 31:
    print("działa")
else:
    print("nie działa")
