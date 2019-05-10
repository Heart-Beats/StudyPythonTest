#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    datetimeformatstr = '%Y-%m-%d %H:%M:%S'
    _timezone = timezone(timedelta(hours=int(tz_str[3:-3])))
    time = datetime.strptime(dt_str, datetimeformatstr).replace(tzinfo=_timezone)
    return time.timestamp()

def get_timedelta(tz_str):
    import re
    timedelta = int(re.split(r'UTC|:', tz_str)[1])
    return timedelta


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
