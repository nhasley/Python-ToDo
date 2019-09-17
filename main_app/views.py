from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# class Item: 
#   def __init__(self, description):
#     self.description = description

# items = [
#     Item('Item 1')
# ]

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'