import os
from django.conf import settings
from django.db import models

class Contact(models.Model):
    email = models.EmailField(verbose_name='이메일')
    content = models.TextField(verbose_name='내용')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'contact_table'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'