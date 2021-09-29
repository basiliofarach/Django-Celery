from django.shortcuts import render
from django.http import HttpResponse

from .tasks import send_mail_func

# Create your views here.


def index(request):
    return HttpResponse('<h1>Task completed</h1>')


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Sent')
