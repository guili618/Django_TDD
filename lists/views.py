from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Item


# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        #new_item_text = request.POST['item_text']
        return redirect('/')
    #else:
        #new_item_text = ""       
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    items = Item.objects.all()
    return render(request,'home.html',{"items":items})