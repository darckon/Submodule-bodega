# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def dashboard(request):
	context = {'welcome': True}
	return render(request, 'bodega/templates/index.html', context)
