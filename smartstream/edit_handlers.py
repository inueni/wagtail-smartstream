from __future__ import absolute_import, unicode_literals

import json

from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from wagtail.wagtailadmin.edit_handlers import BaseStreamFieldPanel
from wagtail.wagtailcore.utils import escape_script

from .blocks import ListBlock, StreamBlock


class SmartStreamFieldPanel(BaseStreamFieldPanel):
    @classmethod
    def html_declarations(cls):
        rendered = []
        member_templates = []
        template_mapper = {}

        for block in cls.block_def.all_blocks():
            if isinstance(block, StreamBlock):
                for name, child_block in block.child_blocks.items():
                    obj_id = str(id(child_block))
                    tpl_id = 'block-tpl-{0}'.format(obj_id)
                    
                    if obj_id not in rendered:
                        member_templates.append(
                            (
                                tpl_id,
                                mark_safe(escape_script(block.render_list_member(name, child_block.get_default(), '__PREFIX__', '')))
                            )
                        )
                        rendered.append(obj_id)
                    
                    template_mapper['{0}-newmember-{1}'.format(block.definition_prefix, name)] = tpl_id
                   
            elif isinstance(block, ListBlock):
                obj_id = str(id(block.child_block))
                tpl_id = 'block-tpl-{0}'.format(obj_id)
                
                if obj_id not in rendered:
                    member_templates.append(
                        (
                            tpl_id,
                            mark_safe(escape_script(block.render_list_member(block.child_block.get_default(), '__PREFIX__', '')))
                        )
                    )
                    rendered.append(obj_id)

                    template_mapper['{0}-newmember'.format(block.definition_prefix)] = tpl_id

        
        
        html_declarations = format_html(
            '\n<script type="text/javascript">\nwindow.sequence_tpl_mapper={0};\n</script>\n',
            mark_safe(json.dumps(template_mapper))
        )
        html_declarations += format_html_join('\n', '<script type="text/template" id="{0}">{1}</script>', member_templates)        
        return html_declarations + format_html('\n{0}', cls.block_def.all_html_declarations())


class StreamFieldPanel(object):
    def __init__(self, field_name, classname=''):
        self.field_name = field_name
        self.classname = classname

    def bind_to_model(self, model):
        return type(str('_StreamFieldPanel'), (SmartStreamFieldPanel,), {
            'model': model,
            'field_name': self.field_name,
            'block_def': model._meta.get_field(self.field_name).stream_block,
            'classname': self.classname,
})