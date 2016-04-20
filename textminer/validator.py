import re

def binary(value):
    return re.match(r'[01]', value)

def binary_even(value):
    return re.match(r'^[10]+[0]$', value)

def hex(value):
    return re.match(r'^[A-F0-9]+$', value)

def word(value):
    return re.match(r'^[\w-]+[a-zA-Z]+$', value)

def words(value, count):
    return re.findall(r'[\w_]', value, count)
    # return re.match(r'^\w+( +\w+)*$', value)
    # return re.match(r'^[\w-]+[a-zA-Z]+( )+$', value)
    # [a-zA-Z0-9_]
