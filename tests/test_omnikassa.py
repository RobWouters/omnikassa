import unittest

from omnikassa import Omnikassa
from omnikassa.exceptions import (
    InvalidSeal,
    InvalidResponseCode,
)


class OmnikassaTests(unittest.TestCase):
    def setUp(self):
        self.settings = {
            'normalReturnUrl': 'https://example.com/omnikassa',
            'automaticResponseUrl': 'https://example.com/callback',
        }
        self.omnikassa = Omnikassa(self.settings)

    def test_seal_fail(self):
        data = 'test data'
        with self.assertRaises(InvalidSeal):
            self.omnikassa.verify_callback(
                {'Seal': 'invalid seal', 'Data': data}
            )

    def test_check_seal(self):
        data = 'test string'
        seal = 'd9d4737039e6066ff5576e75aee5bd02f592e5d49470cc293cd33e7470e46ef9'
        self.assertTrue(self.omnikassa._check_seal(seal, data))

        data = 'test string 1'
        self.assertFalse(self.omnikassa._check_seal(seal, data))

    def test_response_fail(self):
        data = 'responseCode=99'
        seal = self.omnikassa._generate_seal(data)
        with self.assertRaises(InvalidResponseCode):
            self.omnikassa.verify_callback({'Seal': seal, 'Data': data})

    def test_response_success(self):
        data = 'responseCode=00'
        seal = self.omnikassa._generate_seal(data)
        data = self.omnikassa.verify_callback({'Seal': seal, 'Data': data})
        self.assertDictEqual({'responseCode': '00'}, data)
