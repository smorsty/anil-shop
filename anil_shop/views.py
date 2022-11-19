from django.shortcuts import render

def index(request):
    return render(request, "index/index.html")

#Other Pages

def error(request):
    return render(request, "error.html")
