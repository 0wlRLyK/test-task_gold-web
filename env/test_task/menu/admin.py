from django.contrib import admin
from .models import Menu, MenuItem
from modeltranslation.admin import TranslationAdmin

@admin.register(Menu)
class MenuAdmin(TranslationAdmin):
    list_display = ["name"]

@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ["title", "url", "menu"]