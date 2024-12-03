# ##############################################################################
#   Copyright (C) 2024 Connor Flanigan
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import re
from collections import OrderedDict

from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, FormView
from django import forms as django_forms

from . import forms, models


# Create your views here.
class DvdOverviewView(ListView):
    model = models.DiscArchive


class DvdAddNewDiscs(FormView):
    template_name = 'new_discs.html'
    # form_class = forms.NewDiscForm
    success_url = '/add'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_dir = os.environ['DISC_LIBRARY']

        # context['discs'] = [x for x in os.listdir(search_dir)]

        return context

    @property
    def form_class(self):
        fields = OrderedDict()
        for file in os.listdir(os.environ['DISC_LIBRARY']):
            sanitized = re.sub(r'[^A-Za-z0-9]', '_', file)
            fields['file_enabled_'+sanitized] = django_forms.BooleanField(label='', required=False)
            fields['file_'+sanitized] = django_forms.CharField(
                max_length=255,
                required=False,
                initial=file,
                label='',
                disabled=True,
            )

        def validate(zelf):
            pass
            print(zelf)

        fields['validate'] = validate

        # print(fields)
        return type(
            'NewDiscsForm',
            (django_forms.Form,),
            fields,
        )

    def form_valid(self, form):
        # print(form)
        form.validate()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class DvdAddAction(FormView):
    form_class = forms.NewDiscForm

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)
