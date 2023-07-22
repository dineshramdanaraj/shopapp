"""shopapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopping import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name = "home"),
    path('', views.home, name = "home"),
    path("cart/", views.car, name = "cart"),
    path("add_cart/<item_uid>/", views.add_cart, name="add_cart"),
    path('remove_cart_item/<str:cart_item_uid>/', views.remove_cart_item, name='remove_cart_item'),
    path('search_items/', views.search_items, name='search_items'),
    path('category/<category_id>/', views.category_items, name='category_items'),
     path('details/', views.details, name='details'),
    path('increment_quantity/<str:cart_item_uid>/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<str:cart_item_uid>/', views.decrement_quantity, name='decrement_quantity'),
    path("order/", views.orde, name = "order"),
    path("rate_item/<item_uid>", views.rate_item, name = "rate_item"),
    path("payment/<cart_total>", views.payment, name = "payment"),
    path("sucess/", views.sucess, name = "sucess"),
    path('logout/', views.logout_view, name='logout'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()