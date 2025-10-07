import requests
import sys


def main():
    atbilde = requests.get("https://official-joke-api.appspot.com/random_ten")
    if atbilde.status_code == 200:
        print("Pieprasījums ir veiksmīgs")
    else:
        sys.exit()
    saturs = atbilde.json()
    for joks in saturs:
        print(f'Jautājums: {joks["setup"]}\nAtbilde: {joks["punchline"]}')
        print()

main()