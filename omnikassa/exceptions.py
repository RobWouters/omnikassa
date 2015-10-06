class OmnikassaException(Exception):
    pass


class InvalidResponseCode(OmnikassaException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Got responseCode {}'.format(self.data['responseCode'])


class InvalidSeal(OmnikassaException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Invalid seal: {}'.format(self.data)
