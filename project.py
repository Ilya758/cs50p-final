
import json
from time import sleep
from requests import post
from art import *
from constants import API_KEY, API_URL

from entities import StartLoader, TextLoader

def injectCrlf(cb):
    def wrapper(*args, **kwargs):
        print()
        cb(*args, **kwargs)
        print()

    return wrapper

@injectCrlf
def showActualWeather(data):
    for prop in [data['location'], data['current']]:
        for key in prop:
            TextLoader(f'{key.title()}: {prop[key]}', 0.01, trailingCrlf=False)

def askToContinue():
    answer = None

    while not answer or answer.lower() not in ['y', 'n', 'yes', 'no']:
        TextLoader('Do you want to continue? Y(Yes) / N(No)', isInput=True,)
        answer = input(' ')

        if answer.lower() not in ['y', 'n', 'yes', 'no']:
            TextLoader('Enter a valid answer!', crlifyAround=True)
        else:
            match answer.lower():
                case 'y' | 'yes':
                    break
                case _:
                    tprint('Goodbye!')
                    exit(0)


def make_request(city):
    response = post(API_URL, params={
        'q': city,
        'key': API_KEY
    })

    if response.status_code != 200:
        TextLoader('Please check the city name!', crlifyAround=True)
    else:
        data = json.loads(response.text)
        showActualWeather(data)

    return response.status_code

def main():
    try:
        tprint('Hello!')
        StartLoader('Loading')
        sleep(0.5)
        TextLoader('Welcome to the Weatherly!', trailingCrlf=False)

        while True:
            TextLoader('Please enter the city to check the weather:', 0.02, isInput=True, crlifyAround=True)
            city = input(' ')
            make_request(city)
            askToContinue()
    except (EOFError, KeyboardInterrupt) as error:
        if isinstance(error, EOFError) or isinstance(error, KeyboardInterrupt):
            print('\n\n____Unexpected program ending___')
            exit(0)

        print('\n\nSomething went wrong.')
        exit(1)


if __name__ == '__main__':
    main()
