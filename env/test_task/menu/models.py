from django.db import models
from django.utils.translation import gettext as _

class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name of menu"))

    @property
    def parents(self):
        return self.items.filter(parent=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menu")


class MenuItem(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title of menu item"))
    url = models.URLField(verbose_name="URL")
    menu = models.ForeignKey(Menu, verbose_name=_("Parent menu"), null=True, on_delete=models.SET_NULL,
                             related_name="items")
    parent = models.ForeignKey("self", verbose_name=_("Parent menu item"), blank=True, null=True,
                               on_delete=models.SET_NULL, related_name="childs_items")

    def __str__(self):
        return self.title

    @property
    def childs(self):
        return self.childs_items.all()

    class Meta:
        verbose_name = _("Menu item")
        verbose_name_plural = _("Menu items")