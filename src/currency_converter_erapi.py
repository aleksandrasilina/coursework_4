import requests


class CurrencyConverterERAPI:
    """Класс для конвертации валют через API ExchangeRate"""

    def __init__(self, src: str, amount: int | float):
        """Конструктор для конвертера валют"""
        self.src = src  # исходная валюта, которую необходимо конвертировать
        self.dst = "RUB"  # конечная валюта, в которую происходит конвертация
        self.amount = amount
        self.url = f"https://open.er-api.com/v6/latest/{self.src}"

    def get_all_exchange_rates_erapi(self) -> dict:
        """ Запрашивает открытый ExchangeRate API и преобразует его в словарь с курсами валют"""
        data = requests.get(self.url).json()
        if data["result"] == "success":
            return data["rates"]

    def convert_currency_erapi(self) -> int:
        """Конвертирует валюту в рубли"""
        exchange_rates = self.get_all_exchange_rates_erapi()
        return round(exchange_rates[self.dst] * self.amount)
