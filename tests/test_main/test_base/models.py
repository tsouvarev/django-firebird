#-*- utf-8 -*-

from django.db import models


class FieldsTest(models.Model):
    date_field = models.DateTimeField()

class BigS(models.Model):
    s = models.SlugField(max_length=255)
