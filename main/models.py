# -*- encoding: utf-8 -*-
from django.db import models


class Url(models.Model):
	short_url = models.CharField(max_length=10)
	url = models.CharField(max_length=255)

	def __unicode__(self):
		return self.url

	def __str__(self):
		return self.url


class MetaUrl(models.Model):
	url = models.OneToOneField(Url, related_name='meta_url')
	title = models.TextField(verbose_name='New Title')
	description = models.TextField(verbose_name='New Description')
	image = models.URLField(verbose_name='Social Image')

	def __unicode__(self):
		return str(self.url)

	def __str__(self):
		return str(self.url)