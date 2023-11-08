from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def silk(request):
    return HttpResponse('<h1><marquee>heyyy i want dairymilk silk</h1></marquee>')