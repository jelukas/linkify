# -*- encoding: utf-8 -*-s
from urlparse import urlparse
from urllib2 import urlopen
from lxml.html import fromstring, tostring
from lxml import etree as et
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Url

""" 
	<title>Aprende Responsive Design en el curso profesional de Frontend</title>
    <meta name="description" itemprop="description"  content="Crea y programa diseños que se adapten a cualquier pantalla con Responsive Design." />

    <meta property="og:title" itemprop="name" content="Aprende Responsive Design en el curso profesional de Frontend" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://mejorando.la/cursos/frontend-online" />
    <meta property="og:image" itemprop="image" content="https://static.mejorando.la/landing/media/cursos_curso/leonidas-esteban.png" />
    <meta property="og:site_name" content="/" />
    <meta property="fb:admins" content="1030603473" />
"""

def get_page(url):
    html = urlopen(url).read()
    dom = fromstring(html)
    dom.make_links_absolute(url)
    return dom


# doc: https://docs.python.org/2/library/xml.etree.elementtree.html
def ver_web(request, url):
	url_object = get_object_or_404(Url, short_url=url)
	url = url_object.url
	html = get_page(url)

	head = html.findall(".//head")[0]
	title = html.findall(".//title")[0]

	meta_lst = list(html.iter('meta'))
	for meta in meta_lst:
		if 'property' in meta.attrib and  "og" in meta.attrib['property']:
			meta.getparent().remove(meta)
		if 'name' in meta.attrib and  "twitter" in meta.attrib['name']:
			meta.getparent().remove(meta)

	if url_object.meta_url.title:
		title.text = url_object.meta_url.title

	if url_object.meta_url.title:
		meta_og_image = et.Element('meta', property='og:title', content=url_object.meta_url.title)
		head.append(meta_og_image)

	if url_object.meta_url.image:
		meta_og_image = et.Element('meta', property='og:image', itemprop='image', content=url_object.meta_url.image)
		head.append(meta_og_image)

	if url_object.meta_url.description:
		meta_og_description = et.Element('meta', property='og:description', content=url_object.meta_url.description)
		head.append(meta_og_description)

	# Default add site_name = / 
	meta_og_description = et.Element('meta', property='og:site_name', content='/')
	head.append(meta_og_description)


	return HttpResponse(tostring(html))