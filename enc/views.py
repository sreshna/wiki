from django.shortcuts import redirect, render


def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    else:
        return render(request, "enc/welcome.html")