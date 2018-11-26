from django.http import HttpResponse
from django.shortcuts import redirect, render
import wikipedia as wiki


def search_form(request):
    return render(request, 'enc/welcome.html')


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


def suggest(request):
    title = request.GET['q']
    result = wiki.WikipediaPage(title=title).html()
    return render(request, template_name="encapp/wikipage.html",
                  context={"article": {
                      "title": title,
                      "html_content": result
                  }})
