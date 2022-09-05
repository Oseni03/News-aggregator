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
    context["type"] = "Latest"
    return context


def world(request):
      scraper = Scraper()
      context = {
            "news": scraper.world_news(),
            "type": "World",
            }
      return render(request, "news/partials/news_list.html", context)


def business(request):
      scraper = Scraper()
      context = {
            "news": scraper.business_news(),
            "type": "Business"
                 }
      return render(request, "news/partials/news_list.html", context)


def technology(request):
      scraper = Scraper()
      context = {
          "news": scraper.technology_news(),
          "type": "Technology"
      }
      return render(request, "news/partials/news_list.html", context)


def entertainment(request):
      scraper = Scraper()
      context = {
          "news": scraper.entertainment_news(),
          "type": "Entertainment"
      }
      return render(request, "news/partials/news_list.html", context)


def sport(request):
      scraper = Scraper()
      context = {
          "news": scraper.sport_news(),
          "type": "Sport"
      }
      return render(request, "news/partials/news_list.html", context)


def science(request):
      scraper = Scraper()
      context = {
          "news": scraper.science_news(),
          "type": "Science"
      }
      return render(request, "news/partials/news_list.html", context)


def health(request):
      scraper = Scraper()
      context = {
          "news": scraper.health_news(),
          "type": Health
      }
      return render(request, "news/partials/news_list.html", context)