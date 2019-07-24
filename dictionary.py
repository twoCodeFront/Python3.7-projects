
options = {
    'env':'production',
    'db': 'mysqld',
    'version':1.0,
    'show-error': True
}

del options['db']
print(options.get('env'))
# sprawdzi czy klucz istnieje jesli nie zwróci
# nam none jeśli tak poda nam wartośc klucza


options.update({
    'users':'admin',
    'app':0
})


for key in options:
    print(options[key])


print(options.values())
# wypisuje nam wartości

print(options.keys())
# wypisuje nam klucze