# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.test import TestCase

# Create your tests here.

def test(request):
    return HttpResponse('<html>hello django</html')

import MySQLdb

MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'pythontest_db',
    charset = 'utf8'
)