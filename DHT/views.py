from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def test(request):
    return HttpResponse("chaimae nhari")

def dashboard(request):
    return render(request, 'dashbord.html')
def envoyer_alerte():
    send_mail(
        subject="Alerte Temperature",
        message="Temperature superieure a 25 C",
        from_email="morehim.niama01@gmail.com",
        recipient_list=["nhchaimae774@gmail.com"],
        fail_silently=False
    )