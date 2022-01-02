from django.urls import path

from replay import api_views

urlpatterns = [
    path('pentakills', api_views.PentakillReplayListCreateView.as_view()),
]
