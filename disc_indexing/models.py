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

from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class DiscArchive(models.Model):
    archive = models.FileField(blank=True)
    directory = models.FilePathField(blank=True)
    is_processed = models.BooleanField(default=False)

    def clean(self):
        if (self.archive.name != '' and self.directory != '') or (self.archive.name == '' and self.directory == ''):
            raise ValidationError(f'Exactly one of directory or archive must be specified, '
                                  f'{self.archive.name=}, {self.directory=}')
