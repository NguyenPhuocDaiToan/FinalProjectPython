from __future__ import unicode_literals

import re
import ast
import hashlib
from django import template
from django.utils.module_loading import import_string

try:
    # Python 3
    from urllib.parse import (urlencode, urlparse, parse_qs)
except ImportError:
    # Python 2
    from urllib import (urlencode, urlparse, parse_qs)

register = template.Library()


@register.filter
def splitter(value, sep='.'):
    """
    return splited list.
    :param `value` is value to split.
    :param `sep` is splitter.

    usage:
        {{ value|splitter:"/" }}
    """
    return value.split(sep)


@register.filter
def subtract(value, arg):
    return value - arg
