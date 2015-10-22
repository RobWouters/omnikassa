import unittest

from omnikassa import Payment
from omnikassa.constants import Settings


class PaymentTests(unittest.TestCase):
    def setUp(self):
        self.settings = {
            'currencyCode': '978',
            'transactionReference': '123',
            'amount': 123,
            'normalReturnUrl': 'https://example.com/omnikassa',
            'merchantId': Settings.Test.MERCHANT_ID,
        }

    def test_unique_reference_in_test(self):
        p1 = Payment(self.settings)
        p2 = Payment(self.settings)
        self.assertNotEqual(
            p1.settings['transactionReference'],
            p2.settings['transactionReference'],
        )
