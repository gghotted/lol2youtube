from django.urls import path

from replay import views

app_name = 'replay'

urlpatterns = [
    path('', views.PentakillReplayListView.as_view(), name='home'),
    path('list', views.PentakillReplayListView.as_view(), name='list'),
]
