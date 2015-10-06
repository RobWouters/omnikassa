# Omnikassa

[![Build Status](https://travis-ci.org/RobWouters/omnikassa.svg?branch=master)](https://travis-ci.org/RobWouters/omnikassa)

Python library for implementing Omnikassa.

# Generating payment request

    from omnikassa import Omnikassa
    from omnikassa.constants import Currency

    settings = {
        'currencyCode': Currency.EURO,  # Default value, can be overriden per request
        'automaticResponseUrl': 'https://example.com/callback',
        'normalReturnUrl': 'https://example.com/omnikassa',
        'merchantId': '0123456789',
    }
    secret = 'secret key'  # set this to None to use test environment
    
    omnikassa = Omnikassa(settings, secret)
    data = omnikassa.generate_request({
        'transactionReference': 'transaction123',  # unique reference
        'amount': 456,  # in cents
        'orderId': 123,  # optional
    })

`data` contains relevant info to create a form:

    <form action="${url}" method="post" id="form">
        <input type="hidden" name="Seal" value="${seal}">
        <input type="hidden" name="InterfaceVersion" value="${version}">
        <input type="hidden" name="Data" value="${data}">
        <button type="submit">
            Start payment
        </button>
    </form>

# Handling return

    from omnikassa import Omnikassa
    from omnikassa.constants import Currency

    settings = {
        'currencyCode': Currency.EURO,  # Default value, can be overriden 
        'automaticResponseUrl': 'https://example.com/callback',
        'normalReturnUrl': 'https://example.com/omnikassa',
        'merchantId': '0123456789',
    }
    secret = 'secret key'
    
    omnikassa = Omnikassa(settings, secret)
    try:
        data = omnikassa.verify_callback(request.POST)
    except InvalidSeal:
        ...
    except InvalidResponseCode as exc:
        # `exc.data` contains responseData
        ...

    # `data` is a dict of validated omnikassa data
