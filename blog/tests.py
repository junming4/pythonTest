# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.test import TestCase

# Create your tests here.

def test(request):
    return HttpResponse('<html>hello django</html')