from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import re
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth.models import User



    
from instamojo_wrapper import Instamojo
from django.conf import settings

api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');


# Create your views here.
def home(request):
    category_filter = request.GET.get('category')
    items = item.objects.all()
    categories = item_category.objects.all()
    #print(items.first().ratings.rate)
    
    
    if category_filter:
        cat = item_category.objects.get(type_Name = category_filter)
        items = items.filter(type =cat)
   

    context = {
        'items': items,
        'categories': categories,
        
    }

    return render(request, 'home.html', context)


def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user
            user_obj = authenticate(username=username, password=password)
            print(user_obj)
            if user_obj is not None:
                # Log in the user
                login(request, user_obj)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('login')

        except Exception as e:
            print(e)  # Print the exception for debugging
            messages.error(request, "Issue with login")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username already exists")
                return redirect('register')  # Redirect to the same registration page

            user_obj = User.objects.create(username=username, email = email)
            user_obj.set_password(password)
            user_obj.save()

            # Create and save the user profile
            user_profile = UserProfile.objects.create(user=user_obj, email=email)
            user_profile.save()

            messages.success(request, "User created successfully")
            return redirect('login')  

        except Exception as e:
            messages.error(request, "Issue with registration")
            return redirect('register')  

    return render(request, 'register.html')
@login_required
def add_cart(request, item_uid):
    user = request.user
    item_obj = item.objects.get(unique_id=item_uid)
    cart_obj, _ = cart.objects.get_or_create(user=user, is_paid=False)
    cart_items, _ = cart_item.objects.get_or_create(item=item_obj, cart=cart_obj)
    cart_items.quantity +=1
    cart_items.save()
    
    return redirect("/home/")
@login_required
def car(request):
    cart_obj,_ = cart.objects.get_or_create(is_paid=False, user=request.user)
    cart_items = cart_item.objects.filter(cart=cart_obj)
    
    cart_total = 0
    for cart_ite in cart_items:
        cart_total += cart_ite.item.price * cart_ite.quantity
    

    context = {
        'cart': cart_obj,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)
@login_required
def remove_cart_item(request, cart_item_uid):
    cart_ite = cart_item.objects.get(unique_id= cart_item_uid)
    cart_ite.delete()
    return redirect('cart')
@login_required
def orde(request):
    

    cart_obj= cart.objects.filter(is_paid = True, user = request.user)
    
    cart_items = cart_item.objects.filter(cart=cart_obj.first())
    
    cart_total = 0
    for cart_ite in cart_items:
        cart_total += cart_ite.item.price * cart_ite.quantity
    

    context = {
        'orders': cart_obj,
        'cart_total': cart_total,
    }
    return render(request, 'order.html', context)
@login_required
def rate_item(request, item_uid):
    if request.method == 'POST':
        rate = int(request.POST.get('rate'))
        if rate < 1 or rate > 5:
            return redirect('home') 

        item_obj = item.objects.get(unique_id=item_uid)
        rating_obj, created = rating.objects.get_or_create(item_to_rate=item_obj)

        rating_obj.count += 1
        if created:
            rating_obj.rate = rate
        else:    
            rating_obj.rate = (rating_obj.rate * (rating_obj.count - 1) + rate) / rating_obj.count

        rating_obj.save()

        return redirect('order') 

    return redirect('order')

def category_items(request, category_id):
    selected_category = item_category.objects.get(pk=category_id)
    items = item.objects.filter(type=selected_category)

    categories = item_category.objects.all()

    context = {
        'selected_category': selected_category,
        'items': items,
        'categories': categories,
    }

    return render(request, 'filter.html', context)

def search_items(request):
    query = request.GET.get('q')
    results = []

    if query:
        items = item.objects.all()

        for item_obj in items:
            pattern = re.compile(query, re.IGNORECASE)
            if re.search(pattern, item_obj.item_name):
                results.append(item_obj)

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search.html', context)

@login_required
def details(request):
    user = request.user
    userprofile = UserProfile.objects.get(user = user) 
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form = UserProfileForm(instance=userprofile)
    
    context = {
        'user': user,
        'form': form,
        'email': userprofile.email
    }
    return render(request, 'details.html', context)

@login_required
def increment_quantity(request, cart_item_uid):
    cart_item_obj = cart_item.objects.get(unique_id=cart_item_uid)
    cart_item_obj.quantity += 1
    cart_item_obj.save()
    return redirect('cart')
@login_required
def decrement_quantity(request, cart_item_uid):
    cart_item_obj = cart_item.objects.get(unique_id=cart_item_uid)
    if cart_item_obj.quantity > 1:
        cart_item_obj.quantity -= 1
        cart_item_obj.save()
    return redirect('cart')
@login_required
def payment(request, cart_total):
    userprofil = UserProfile.objects.get(user = request.user)
    cart_obj = cart.objects.get(user = request.user)
   
    cart_obj.save()
    print(userprofil.email, userprofil.ph_no)
    response = api.payment_request_create(
        amount = cart_total,
        purpose = "order",
        buyer_name = request.user.username,
        email =     request.user.email,
        redirect_url = 'http://127.0.0.1:8000/sucess',
        phone = userprofil.ph_no

    )
    print(response)
    payment_url = response['payment_request']['longurl']
    cart_obj.instamojo_id = response['payment_request']['id']
    return HttpResponseRedirect(payment_url)
@login_required
def sucess(request):
    pay_req_id = request.GET.get('payment_request__id')
    cart_obj = cart.objects.get(instamojo_id = pay_req_id)
    cart_obj.is_paid = True
    cart_obj.save()
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login') 