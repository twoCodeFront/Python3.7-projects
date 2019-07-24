
# oddzielone są () a nie jak listy []
# są nie modyfikowalne

#
my_tuple = (30,22,12,11,34,55,66,77,43,234,656,323,1)
#
new_tuple = my_tuple[:3]
# tworzymy nowego tupla i zaciągamy z starego pierwsze 3 parametry
#
print( 2 in new_tuple)
# sprawdzamy czy 2ka pojawia się w new_tuple
#

my_list = [10,4,12,14,7,2,5]
tuple = tuple(my_list)
print(max(tuple))
# sprawdzenie makstmalnej wartości

print(min(tuple))
# minimalna ilość

print(sum(tuple))
# sumowanie wszystkich wartości które się tu znajdują

a,b,c,d,e,f,g = tuple
print(b)
# wielokrotne przypisanie a= 10 b=4 ..

