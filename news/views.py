from django.shortcuts import render
from django.views import generic

from .scraper import latest

# Create your views here.
class HomeView(generic.TemplateView):
  template_name = "news/index.html"
  
  def get_context_data(self, *args, **kwargs):
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["news"] = latest()
    return context