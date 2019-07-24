# coding=utf-8
a = set([1,3,4,52,34,2,4,53,5,6,5])
# każda wartość musi być unikalna
b = set([1,3,4])
print(a.intersection(b))
# pokaże tylko to co jest zawarte w zbiorze a i w b
# pokaze tylko 4

print(a.difference(b))
# zbiory które nie występują /różnica tych dwóch zbiorów

print(a.union(b))
# łączenie setów

print(a.symmetric_difference(b))
# wszystkie elementy unikalne dla a i b (wystepują tylko w tych zbiorach

