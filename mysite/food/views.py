from tempfile import template

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ItemForm
from .models import Item
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
# function based view
#
def index(request):
    Item_list =  Item.objects.all()
    print(Item_list)
    # context =
    return render(request,'food/index.html',{"Item_lists": Item_list})


# class-based view
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'Item_lists'

def item(request):
    return HttpResponse("<h1>Maximum effort</h1>")

# fun-based view

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context = {
        "item" : item
    }
    return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

#     fun-based view
#
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form})

# classs-based create view
#
class CreateItem(CreateView):
    model = Item
    fields = ['Item_name','Item_desc','Item_Price','Item_image']
    template_name = 'food/item_form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



def update_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/delete_item.html',{'item':item})









