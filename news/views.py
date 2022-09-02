from django.shortcuts import render
from django.views import generic

from .scraper import latest

# Create your views here.
class HomeView(generic.TemplateView):
  template_name = "news/index.html"
  
  def get(self, *args, **kwargs):
    if self.request.htmx:
      context = {"news": latest()}
      return render(self.request, "news/partials/news_list.html", context)
    return super().get(*args, **kwargs)
  
  def get_context_data(self, *args, **kwargs):
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["news"] = latest()
    return context