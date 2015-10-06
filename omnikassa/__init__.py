import logging

from hashlib import sha256
from hmac import compare_digest


from .payment import Payment
from .exceptions import (
    OmnikassaException,
    InvalidResponseCode,
    InvalidSeal,
)
from .constants import (
    Settings,
    ResponseCode,
)
from .helpers import str_to_data

log = logging.getLogger(__name__)


class Omnikassa:
    def __init__(self, settings, secret=None):
        if secret:
            self.url = Settings.URL
            self.secret = secret
        else:
            settings['merchantId'] = Settings.Test.MERCHANT_ID
            self.secret = Settings.Test.SECRET_KEY
            self.url = Settings.Test.URL
        self.settings = self._validate_settings(settings)

    def _validate_settings(self, settings):
        if not settings.get('merchantId'):
            raise OmnikassaException('merchantId is required.')
        if not settings.get('normalReturnUrl'):
            raise OmnikassaException('normalReturnUrl is required.')
        if not settings.get('automaticResponseUrl'):
            raise OmnikassaException('automaticResponseUrl is required.')
        if not settings.get('keyVersion'):
            settings['keyVersion'] = '1'
        return settings

    def generate_request(self, settings):
        payment = self.settings.copy()
        payment.update(settings)
        payment = Payment(payment)
        return {
            'url': self.url,
            'data': payment,
            'seal': self._generate_seal(payment),
            'version': Settings.VERSION,
        }

    def verify_callback(self, data):
        if not self._check_seal(data['Seal'], data['Data']):
            raise InvalidSeal(data)
        data = str_to_data(data['Data'])
        if data['responseCode'] != ResponseCode.SUCCESS:
            raise InvalidResponseCode(data)
        return data

    def _generate_seal(self, data):
        data = str(data) + self.secret
        return sha256(data.encode()).hexdigest()

    def _check_seal(self, seal, data):
        return compare_digest(seal, self._generate_seal(data))
