from django.http import HttpResponse
from django.shortcuts import render
import wikipedia as wiki
from django.views.generic import DetailView
from django.views.generic.base import View, TemplateView

from encapp.models import Favorites


class HomeView(TemplateView):
    template_name = "enc/welcome.html"


def search(request):
    try:
        title = request.GET['q']
        result = wiki.page(title=title).html()
    except wiki.DisambiguationError as e:
        return render(request, template_name="encapp/wikipage.html",
                      context={"options": e.options})
    except:
        return HttpResponse('You submitted an empty form')
    return render(request, template_name="encapp/wikipage.html",
                  context={"article": {
                      "title": title,
                      "html_content": result
                  }})


class FavoritesCreateView(View):
    def get(self, request, *args, **kwargs):
        title = request.GET['title']
        fav = Favorites.objects.create(title=title, user=request.user)
        return render(request, template_name="encapp/wikipage.html",
                      context={"favorites": fav})


class FavoritesDetailView(TemplateView):
    template_name = "encapp/favorite.html"

    def get(self, request, *args, **kwargs):
        title = request.GET['q']
        result = wiki.page(title=title).html()
        context = {"article": {
            "title": title,
            "html_content": result
        }}
        return self.render_to_response(context)


def language(request):
    lang = request.GET['lang_option']
    result = wiki.set_lang(lang)
    return render(request, template_name="encapp/wikipage.html",
                  context={"html_content": result})
