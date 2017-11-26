# wagtail-smartstream

Proof of concept Wagtail StreamFieldPanel that avoids unnecessary rendering of templates used for adding StreamField blocks. 

## Usage

Add `smartstream` to `INSTALLED_APPS`. 

On your `Page` models, substitute `wagtail.wagtailadmin.edit_handlers.StreamFieldPanel` with `smartstream.edit_handlers.StreamFieldPanel`

When defining StreamField blocks, use `smartstream.blocks.ListBlock` and `smartstream.blocks.StreamBlock` in place of Wagtail variants.