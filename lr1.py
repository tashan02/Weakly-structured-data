from zeep import Client 

def get_request_input():
    print("Допустимые категории запросов:")
    print("- Список континентов")
    print("- Информация о стране")
    print("- Список всех стран")
    print()

    category = input("Введите категорию запроса: ")

    print("Доступные методы для выбранной категории:")
    print()

    if category == "Список континентов":
        wsdl_url = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    elif category == "Информация о стране":
        wsdl_url = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    elif category == "Список всех стран":
        wsdl_url = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    else:
        print("Выбранная категория запроса не поддерживается.")
        return None

    client = Client(wsdl_url)

    services = client.service

    methods = services.__dir__()
    for method in methods:
        print(f"- {method}")

    method = input("Введите метод: ")

    if method not in methods:
        print("Выбранный метод не существует.")
        return None

    if method == "CurrencyName":
        sCurrencyISOCode = input("Введите код валюты: ")

        if not sCurrencyISOCode:
            print("Необходимо ввести код валюты.")
            return None

        result = getattr(services, method)(sCurrencyISOCode)
    else:
        sISOCode = input("Введите ISO-код страны: ")

        if not sISOCode:
            print("Необходимо ввести ISO-код страны.")
            return None

        try:
            result = getattr(services, method)(sISOCode)
        except TypeError:
            print("Введенный ISO-код страны некорректный.")
            return None

    return result

while True: 
    result = get_request_input() 
    if not result: 
        break 
    print(result)