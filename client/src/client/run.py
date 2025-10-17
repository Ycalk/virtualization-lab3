import requests


def run():
    response = requests.get("http://server:8080/file", timeout=10)
    if response.status_code == 200:
        print("Ответ сервера\n")
        print(response.text)
    else:
        print("Произошла ошибка")
