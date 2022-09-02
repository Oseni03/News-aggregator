from django.shortcuts import render
from django.views import generic

from .scraper import Scraper

# Create your views here.
class HomeView(generic.TemplateView):
  template_name = "news/index.html"
  
  def get(self, *args, **kwargs):
    scraper = Scraper()
    if self.request.htmx:
      context = {"news": scraper.latest()}
      return render(self.request, "news/partials/news_list.html", context)
    return super().get(*args, **kwargs)
  
  def get_context_data(self, *args, **kwargs):
    scraper = Scraper()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["news"] = scraper.latest()
    return context