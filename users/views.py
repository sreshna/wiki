from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from encapp.models import Favorites


@login_required
def home(request):
    favorites = Favorites.objects.all().filter(user=request.user)
    return render(request, template_name="users/home.html",
                  context={"favorites": favorites})
    # return render(request, "users/home.html")


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
