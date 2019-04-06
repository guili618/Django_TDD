from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Item,List


# Create your views here.

def home_page(request):
    
    #Item.objects.create(text=request.POST['item_text'])
        #new_item_text = request.POST['item_text']
    #return redirect('/lists/the-only-list-in-the-world/')
    #else:
        #new_item_text = ""       
    #if request.method == 'POST':
    return render(request,'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{"items":items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
