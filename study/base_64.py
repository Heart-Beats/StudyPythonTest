#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64


def safe_base64_decode(s):
    def get_decode_str(decodedata):
        if isinstance(decodedata, bytes):
            decodedata = decodedata.decode('utf-8')
        return decodedata

    def base64_decode(base64str):
        base64_lostlength = (4 - len(base64str) % 4) % 4
        base64str = str.ljust(base64str, len(base64str) + base64_lostlength, '=')
        return base64.b64decode(base64str)

    return base64_decode(get_decode_str(s))


print(safe_base64_decode(b'YWJjZA=='))
print(safe_base64_decode('YWJjZA'))

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
