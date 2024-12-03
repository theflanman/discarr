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

from django import forms
from django.forms import formset_factory


class UnindexedDiscForm(forms.Form):
    enabled = forms.BooleanField(required=False)
    disc_name = forms.TextInput()


unindexed_disc_formset = formset_factory(UnindexedDiscForm)


class NewDiscForm(forms.Form):

    def __init__(self, *args, **kwargs):
        print(args)
        super().__init__(*args, **kwargs)


