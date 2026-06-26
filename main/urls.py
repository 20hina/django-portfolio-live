from django.urls import path
from . import views

urlpatterns = [
    path('',           views.login_view,  name='login'),
    path('portfolio/', views.index,       name='portfolio'),
    path('logout/',    views.logout_view, name='logout'),
]