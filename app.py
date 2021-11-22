def make_country():
    x = {'name':country, 'city':capital}
    print('The capital of {} is {}'.format(x['name'], x['city']))
country = input('your country:')
capital = input('your capital:')
make_country()