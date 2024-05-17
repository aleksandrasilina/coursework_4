def test_currency_converter_erapi_init(cc_api):
    """Тестирует конструктор для конвертера валют"""
    assert cc_api.src == 'CNY'
    assert cc_api.dst == 'RUB'
    assert cc_api.amount == 1000
    assert cc_api.url == f"https://open.er-api.com/v6/latest/CNY"


def test_currency_converter_erapi_get_all_exchange_rates_erapi(cc_api):
    """Тестирует метод для запроса ExchangeRate API и преобразования его в словарь с курсами валют"""
    assert len(cc_api.get_all_exchange_rates_erapi()) == 162


def test_currency_converter_erapi_convert_currency_erapi(cc_api):
    """Тестирует метод для конвертации валюты в рубли"""
    assert cc_api.convert_currency_erapi() == 12582
