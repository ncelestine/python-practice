from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('goodbye/', views.goodbye, name='goodbye'),  # Goodbye page
]
