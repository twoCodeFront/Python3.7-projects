def zbiera(a,*args,**dict_args):
    print(a)
    print(args)
#     print(args[2])
    print(dict_args)


zbiera(2,3,4,"true",True,False,user='admin',version=1.0,env = 'production')
# wszystkie argumenty zebrane od 2giego zawarte są w tuple
# nastpene zostana zebrane do dictionary


def ng(a,b):
    return a+b,a-b,a*b

r = ng(3,4)
# zwroci nam tuple

print(r[2])