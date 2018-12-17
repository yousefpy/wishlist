from django.shortcuts import render, redirect
from items.models import Item , FavoriteItem
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def item_list(request):
    items = Item.objects.all()
    fav_item = []
    if request.user.is_authenticated:
        user_fav = FavoriteItem.objects.filter(user=request.user)
        for fav in user_fav:
            fav_item.append(fav.item)

    query = request.GET.get('q')
    if query:
        items = items.filter(name__contains=query)
    context = {
        "items": items,
        "favs" : fav_item,
    }
    return render(request, 'item_list.html', context)

def faving_item(request, item_id):
    item_obj = Item.objects.get(id=item_id)
    fav_item, create = FavoriteItem.objects.get_or_create(item=item_obj, user=request.user)

    if create:
        action = "favorite"
    else:
        action = "unfavorite"
        fav_item.delete()

    data = {
    "action" : action,
    }

    return JsonResponse(data)

def user_favorite_list(request):
    fav_items = FavoriteItem.objects.filter(user=request.user)

    query = request.GET.get('q')
    if query:
        fav_items = fav_items.filter(item__name__contains=query)

    context = {
    "fav_items" : fav_items,
    }
    return render(request, 'favorite_list.html', context)

def item_detail(request, item_id):
    context = {
        "item": Item.objects.get(id=item_id)
    }
    return render(request, 'item_detail.html', context)

def user_register(request):
    register_form = UserRegisterForm()
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('item-list')
    context = {
        "register_form": register_form
    }
    return render(request, 'user_register.html', context)

def user_login(request):
    login_form = UserLoginForm()
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('item-list')
    context = {
        "login_form": login_form
    }
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)

    return redirect('item-list')