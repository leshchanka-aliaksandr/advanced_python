import requests
import json


class Money:
    """Money class for currency calculator"""
    api = "86759a1a613902c1877c7f1b"

    def __init__(self, count, currency="USD"):
        self._count = count
        self._currency = currency

    def __str__(self):
        return "{:.2f} {}".format(self._count, self._currency)

    def __add__(self, other):
        count = self._count + other._count / self._currency_rate(
            self._currency, other._currency)
        return Money(count, self._currency)

    def __radd__(self, other):
        if isinstance(other, Money):
            count = self._count + other._count / self._currency_rate(
                self._currency, other._currency)
            return Money(count, self._currency)
        else:
            return self

    def __iadd__(self, other):
        return Money(self._count + other._count, self._currency)

    def __mul__(self, other):
        return Money(self._count * other, self._currency)

    def __rmul__(self, other):
        return Money(self._count * other, self._currency)

    def _currency_rate(self, f, t):
        url = f"https://v3.exchangerate-api.com/bulk/{self.api}/{f}"
        request = json.loads(requests.get(url).text)
        return request["rates"][t]


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
