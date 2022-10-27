from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail



def mail1(request):
    send_mail(
        'Test Mail Using Django Framework',
        'Hello Sir/Mam',
        'kjagadeesh620@gmail.com',
        ['2100032246@kluniversity.in'],
        fail_silently = False,
    )
    return print('Mail Sent')