from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("Wa are at about")
def contact(request):
    return HttpResponse("Wa are at contact")
def tracker(request):
    return HttpResponse("Wa are at Tracker")
def search(request):
    return HttpResponse("Wa are at Search")
def productview(request):
    return HttpResponse("Wa are at Product View")
def checkout(request):
    return HttpResponse("Wa are at checkout")
