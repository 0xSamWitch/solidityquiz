# -*- coding: utf-8 -*-
import base64
import json
import markdown
import re
import urllib.parse

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()

def format_reference(match):
    full_reference = match.group(0)
    section_name = match.group('section_name')
    paragraph_number = match.group('paragraph')
    full_link = "https://timsong-cpp.github.io/cppwp/n4659/" + section_name
    if paragraph_number:
        full_link = full_link + "#" + paragraph_number
    return "<em><a href=\"" + full_link + "\">" + full_reference + "</a></em>"

def standard_ref(text):
    section_name = u'(\[(?P<section_name>[\w:]+(\.[\w:]+)*)\])'
    possible_paragraph = u'(¶(?P<paragraph>\d+(\.\d+)*))*'
    regex = re.compile('§(' + section_name + possible_paragraph + ')')
    return re.sub(regex, format_reference, text)

def custom_linebreaks(text):
    return (text
        .replace("\n", "<br />")
        .replace("</p><br />", "</p>")
        .replace("<br /><p>", "<p>")
        .replace("</pre><br />", "</pre>"))

@register.filter(needs_autoescape=True)
def to_html(text, autoescape=None):
    return mark_safe(
        standard_ref(
            custom_linebreaks(
                markdown.markdown(text))))
