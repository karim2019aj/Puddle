from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout


def index(request):
    items = Item.objects.filter(is_sold='False')[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items' : items,
    })
def itemsInCategory(request, category_name):
    category = Category.objects.get(name=category_name)

    items = Item.objects.filter(category=category)
    print(items)
    return render(request, 'core/category.html', {
        'items' : items,
    })



def contact(request):
    return render(request, 'core/contact.html')  

def signup(request):
    if request.method == 'POST':
        print(request)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:        
        form = SignupForm()  
        print(request) 
    return render(request, 'core/signup.html',{
        'form' : form
    }) 

def logout_view(request):
    logout(request)
    return redirect('/')