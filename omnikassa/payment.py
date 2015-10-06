from .exceptions import OmnikassaException
from .helpers import data_to_str


class Payment:
    def __init__(self, settings):
        self.settings = self._validate_settings(settings)

    def _validate_settings(self, settings):
        if not settings.get('currencyCode'):
            raise OmnikassaException('currencyCode is required.')

        if not settings.get('transactionReference'):
            raise OmnikassaException('transactionReference is required.')

        if not settings.get('amount'):
            raise OmnikassaException('amount is required.')
        if type(settings['amount']) != int:
            raise OmnikassaException('amount should be an integer (cents).')

        if not settings.get('normalReturnUrl'):
            raise OmnikassaException('normalReturnUrl is required.')

        return settings

    def __str__(self):
        return data_to_str(self.settings)
