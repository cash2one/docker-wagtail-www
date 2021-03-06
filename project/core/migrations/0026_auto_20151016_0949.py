# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20151015_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universalstreampage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('teaser_area', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock()), ('content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/teaser_area.html')), ('quotation', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock(help_text='quotation marks (“...”) will be added automatically')), ('name', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/quotation.html')), ('one_column_text', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock()),), template='core/blocks/one_column_text.html')), ('two_column_50_50_text', wagtail.wagtailcore.blocks.StructBlock((('left_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('right_content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/two_column_50_50_text.html')), ('two_column_66_33_text', wagtail.wagtailcore.blocks.StructBlock((('left_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('right_content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/two_column_66_33_text.html')), ('three_column_33_33_33_text', wagtail.wagtailcore.blocks.StructBlock((('left_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('center_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('right_content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/three_column_33_33_33_text.html')), ('four_column_text', wagtail.wagtailcore.blocks.StructBlock((('col1_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col2_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col3_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col4_content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/four_column_text.html')), ('six_column_text', wagtail.wagtailcore.blocks.StructBlock((('col1_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col2_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col3_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col4_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col5_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('col6_content', wagtail.wagtailcore.blocks.RichTextBlock())), template='core/blocks/six_column_text.html')), ('call_to_action_area', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('button_label', wagtail.wagtailcore.blocks.CharBlock()), ('button_link', wagtail.wagtailcore.blocks.URLBlock())), template='core/blocks/call_to_action_area.html')), ('raw_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()),), template='core/blocks/raw_html.html')))),
            preserve_default=True,
        ),
    ]
