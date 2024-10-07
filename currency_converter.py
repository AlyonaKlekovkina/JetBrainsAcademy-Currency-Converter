import requests
import json


def retrieve_json_data(currency):
    url = 'http://www.floatrates.com/daily/{}.json'.format(currency)
    response = requests.get(url).json()
    json_string = json.dumps(response)
    loaded_dictionary = json.loads(json_string)
    return loaded_dictionary


def set_default_dict(json_dic, default_currency):
    rates_dict = {}
    if default_currency == 'usd':
        eur = json_dic['eur']['rate']
        rates_dict = {'eur': eur}
    if default_currency == 'eur':
        usd = json_dic['usd']['rate']
        rates_dict = {'usd': usd}
    elif default_currency != 'usd' and default_currency != 'eur':
        usd = json_dic['usd']['rate']
        eur = json_dic['eur']['rate']
        rates_dict = {'usd': usd, 'eur': eur}
    return rates_dict


def update_dictionary(rates_dict, currency, updated_dictionary):
    rate = rates_dict[currency]['rate']
    updated_dictionary.update({currency: rate})
    return updated_dictionary


default_currency_input = input().lower()
dictionary_with_data = retrieve_json_data(default_currency_input)
cached_dictionary = set_default_dict(dictionary_with_data, default_currency_input)

while True:
    currency_code = input().lower()
    if len(currency_code) == 0:
        break
    amount_of_money = input()

    if currency_code in cached_dictionary:
        result = float(amount_of_money) * cached_dictionary[currency_code]
        print('Checking the cache...')
        print('Oh! It is in the cache!')
        print('You received {:0.2f} {}.'.format(result, currency_code.upper()))
    else:
        updated_dictionary = update_dictionary(dictionary_with_data, currency_code, cached_dictionary)
        print('Checking the cache...')
        print('Sorry, but it is not in the cache!')
        result = float(amount_of_money) * updated_dictionary[currency_code]
        print('You received {:0.2f} {}.'.format(result, currency_code.upper()))
