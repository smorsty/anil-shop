from django.shortcuts import render
from shop.forms import PickTypeForm

def index(request):
    if request.method == 'GET':
        form = PickTypeForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['product_type']:
                pass

    return render(request, "index/index.html")

#Other Pages

def error(request):
    return render(request, "error.html")
