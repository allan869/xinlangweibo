#_*_coding:utf-8_*_
__author__ = 'zhangkai'


import django
import redis

def redis_conn(django_settings):
    #print(django_settings.REDIS_CONN)
    pool = redis.ConnectionPool(host=django_settings.REDIS_CONN['host'], port=django_settings.REDIS_CONN['port'],db=0)
    r = redis.Redis(connection_pool=pool)
    return  r