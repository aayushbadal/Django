from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlogPage(generic.TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlogDetailPage(generic.TemplateView):
    template_name = "single.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlogDetailPage(generic.TemplateView):
    template_name = "single.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
