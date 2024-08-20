from django.urls import path
from .views.ui_views import track_list

urlpatterns = [
    path('ui_tracks/', track_list, name='ui_tracks'),
]
