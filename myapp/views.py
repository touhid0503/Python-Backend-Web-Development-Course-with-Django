from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Feature


# def count(request)
# Create your views here.
def index(request):
    # pass
    # return HttpResponse("<h1><i>Hi Touhid</i></h1>")
    # name = "Bittu Vai"
    # age = 50
    # feature1 = Feature()
    # feature1.isTrue=True
    # feature1.id = 0
    # feature1.name = "Fast"
    # feature1.details = "Our Service is very quick"

    # feature2 = Feature()
    # feature2.isTrue=True
    # feature2.id = 1
    # feature2.name = "Reliable"
    # feature2.details = "Our Service is very reliable"

    # feature3 = Feature()
    # feature3.isTrue=False
    # feature3.id = 2
    # feature3.name = "Easy to Use"
    # feature3.details = "Our Service is very easy to use"

    # feature4 = Feature()
    # feature4.isTrue=True
    # feature4.id = 3
    # feature4.name = "Affordable"
    # feature4.details = "Our Service is very affordable"

    # features = [feature1, feature2, feature3, feature4]

    features = Feature.objects.all()
    return render(request, "index.html", {"features": features})


def counter(request):
    words = request.POST["words"]
    amount_words = len(words.split())
    return render(request, "counter.html", {"amount_words": amount_words})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password Not The Same")
            return redirect("register")
    else:
        return render(request, "register.html")

    # return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
