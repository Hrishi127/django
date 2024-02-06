from django.urls import path
from .views import NotesView

urlpatterns = [
    path('post/', NotesView.as_view(), name='post'),
    path('get', NotesView.as_view(), name='get'),
    path('delete/<int:pk>', NotesView.as_view(), name='delete'),
]