# -*- coding: utf-8 -*-
from django.db import models

class upload_files(models.Model):
    file_name = models.CharField(verbose_name='文件名', max_length=64, blank=False)
    file_size = models.IntegerField(verbose_name='文件大小', blank=False)
    upload_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True )
    upload_user = models.CharField(verbose_name='上传人', max_length=32, blank=False)

class server_list(models.Model):
    server_name = models.CharField(verbose_name='服务器名', max_length=32, blank=False, unique=True)
    inner_ip = models.CharField(verbose_name='内部IP', max_length=64, blank=False)
    external_ip = models.CharField(verbose_name='外部IP', max_length=64, blank=False)
    os = models.CharField(verbose_name='系统', max_length=64, blank=False)
    belong_to = models.CharField(verbose_name='属于哪个服务器', max_length=64, blank=False)
    status = models.BooleanField(verbose_name='状态')

class command_template(models.Model):
    description = models.CharField(verbose_name='描述', max_length=32, blank=False, unique=True)
    cmd = models.CharField(verbose_name='命令', max_length=1024, blank=False)