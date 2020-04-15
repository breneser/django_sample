#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

import datetime


class HelloView(TemplateView):
    now = datetime.datetime.now()
