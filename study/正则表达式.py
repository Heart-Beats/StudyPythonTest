#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def is_valid_email(addr):
    if re.match(r'^.+@(gmail|microsoft).com$', addr):
        return True
    return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    m=re.match(r'^.*?([a-zA-Z]+\s*[a-zA-Z]*).*?@\w+\.\w+$',addr)
    if m:
        return m.group(1)
    return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

