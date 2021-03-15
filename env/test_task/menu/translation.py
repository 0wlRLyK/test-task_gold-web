from modeltranslation.translator import register, TranslationOptions
from .models import Menu, MenuItem


@register(Menu)
class MenuOptions(TranslationOptions):
    fields = ('name',)


@register(MenuItem)
class MenuItmeOptions(TranslationOptions):
    fields = ('title',)