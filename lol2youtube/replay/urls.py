from django.urls import path

from replay import views

urlpatterns = [
    path('pentakills', views.PentakillReplayCreateView.as_view()),
]
