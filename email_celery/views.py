from django.shortcuts import render, redirect
from django.http import HttpResponse

from .tasks import send_mail_func

# Create your views here.


def index(request):
    return render(request, 'email_celery/celery_page.html')


def send_mail_to_all(request):
    send_mail_func.delay()
    return redirect('/celery')
