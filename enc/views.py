from django.shortcuts import redirect, render


def welcome(request):
    return render(request, "enc/welcome.html")