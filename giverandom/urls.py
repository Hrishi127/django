from django.urls import path
from .views import RandomNumberView

urlpatterns = [
    path('randomnumber/', RandomNumberView.as_view(), name='random_number'),
]