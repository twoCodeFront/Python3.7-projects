# 2 warunki ilość lajków - 500
# ilośc udostępniej <=100

#
# like = input("ilość lajków : ")
# udostepnienia = input("ilość udostępnień :")
#
# if int(like) >= 500 and int(udostepnienia) >= 100 :
#     print("promocja rozpoczyna się !")
# elif int(like) < 500:
#     print("brakuje lajków")
# elif int(udostepnienia) <=100:
#     print("brakuje udostepnień")
# else:
#     print("brakuje wszystkiego")


# todo zamówileś pizze lub napój w dzień nie będący weekendem dajemy kupon
# jeśli jest weekend to wyświetlamy informację że jest weekend i nie ma kupony
# jeśli brakuje pizzu lub napoju w zamówieniu to wyskakuje informacja o braku tego lub tehgo


Weekend = False
pizza = False
Cola = True

if Weekend == False and pizza == True and Cola == True:
    print("gratulacje otrzymujesz kupon")
elif Weekend == True :
    print("promocja dotyczy tylko dni w tygodniu")
elif pizza == False or Cola == False:
    print("zabrakło w zamówieniu coli lub pizzy")
