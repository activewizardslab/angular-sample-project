from random import uniform, randrange, getrandbits
from datetime import timedelta, datetime
import time

from .models import TemperatureLog, MultiDataLog, StatusLog

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def create_fake_temperature_log(user_pk, timestamp=None):
    if not timestamp:
        timestamp = time.time()

    temp_log = TemperatureLog(
        user_id=user_pk,
        timestamp=timestamp,
        field1_data=uniform(0.0, 50.0)
    )
    temp_log.save()


def create_fake_multi_data_log(user_pk, timestamp=None):
    if not timestamp:
        timestamp = time.time()

    multi_data_log = MultiDataLog(
        user_id=user_pk,
        timestamp=timestamp,
        field1_data=uniform(0.0, 50.0),
        field2_data=uniform(0.0, 50.0),
        field3_data=uniform(0.0, 50.0),
        field4_data=uniform(0.0, 50.0),
        field5_data=uniform(0.0, 50.0)
    )
    multi_data_log.save()


def create_fake_status_log(user_pk, timestamp=None):
    if not timestamp:
        timestamp = time.time()

    status_log = StatusLog(
        user_id=user_pk,
        timestamp=timestamp,
        field1_data=getrandbits(1)
    )
    status_log.save()


def initial_fake_data(user):
    d1 = datetime.strptime('3/15/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('3/20/2016 4:50 AM', '%m/%d/%Y %I:%M %p')

    for i in range(30):
        create_fake_temperature_log(user.pk, random_date(d1, d2).timestamp())
        create_fake_multi_data_log(user.pk, random_date(d1, d2).timestamp())
        create_fake_status_log(user.pk, random_date(d1, d2).timestamp())
