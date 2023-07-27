from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import mobile, stocks


def index(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data['log'], password=data['psw'])
        if user != None:
            return render(request, 'main.html')
        else:
            err = f"Ошибка! Данного пользователя не существует!"
            return render(request, 'index.html', {"err": err})
    return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        data = request.POST
        new_user = User.objects.create_user(
            data['mail'], data['log'], data['psw'])
        new_user.save()
        congr = f"Вы успешно зарегистрировались и можете войти под своей учетной записью."
        return render(request, 'main.html', {"congr": congr})
    return render(request, 'reg.html')


def main(request):
    query_res = mobile.objects.all()
    return render(request, 'main.html', {'query_res': query_res})
