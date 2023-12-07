from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="great"),
    path("thiago", views.thiago, name="thiago"),
    path("david", views.david, name="david")
]
 