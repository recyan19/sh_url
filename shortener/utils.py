from shortener.models import Url

import random
import string


def get_short_code_for_url():
    length = 7
    charset = string.ascii_lowercase + string.digits + string.ascii_uppercase

    while True:
        url_id = ''.join(random.choice(charset) for x in range(length))

        try:
            tmp = Url.objects.get(url_id=url_id)
        except Url.DoesNotExist:
            return url_id
