from django.shortcuts import render
from django.views import generic
from .models import Menu

class MainPageView(generic.TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = Menu.objects.first()
        return context