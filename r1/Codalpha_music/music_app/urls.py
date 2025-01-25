from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL now points to the home view
    path('predict/', views.predict, name='predict'),
]
