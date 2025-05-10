import random
from django.core.cache import cache


def generate_code():
    code = str(random.randint(100000, 999999))
    return code
