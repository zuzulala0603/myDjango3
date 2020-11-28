import os
from django.conf import settings
from django.db import models

class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post_table'
        verbose_name = 'post'
        verbose_name_plural = 'posts'