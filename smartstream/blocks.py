from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.staticfiles.templatetags.staticfiles import static
from wagtail.wagtailcore.blocks import (
    ListBlock as WagtailListBlock, 
    StreamBlock as WagtailStreamBlock,
)

class SequenceBlockMixin(object):
    def html_declarations(self):
        return ''

    def js_initializer(self):
        js_init = super(SequenceBlockMixin, self).js_initializer()

        return "Smart" + js_init


class ListBlock(SequenceBlockMixin, WagtailListBlock):
    def html_declarations(self):
        return ''

    @property
    def media(self):
        return forms.Media(js=[static('wagtailadmin/js/blocks/sequence.js'), static('smartstream/js/list.js')])


class StreamBlock(SequenceBlockMixin, WagtailStreamBlock):
    @property
    def media(self):
        return forms.Media(js=[static('wagtailadmin/js/blocks/sequence.js'), static('smartstream/js/stream.js')])