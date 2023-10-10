from django.shortcuts import render
from django.http import HttpResponse
import datetime

#Index 
def index(request):

#Cookies
def cookies(request):
    dico_cookies = request.COOKIES