from django.urls import path
from django.contrib.auth import views as auth_viewd

from . import views
from .forms import LoginForm

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<str:category_name>/', views.itemsInCategory, name='itemsInCategory'),
    path('contact/', views.contact, name='contact'),
    path('signup/',views.signup, name='signup'),
    path('logout',views.logout_view, name='logout'),
    path('login/', auth_viewd.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),

]