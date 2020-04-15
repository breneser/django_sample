#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

import datetime


class HelloView(TemplateView):

    template_name = 'django_sample/hello.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['thedate'] = datetime.datetime.now()
        return context
