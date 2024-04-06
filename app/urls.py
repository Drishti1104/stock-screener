from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path("", Index, name="index"),
    path("login", Login, name="login"),
    path("register", Register, name="register"),
    path("logout", Logout, name="logout"),
    path("samp", Samp, name="samp"),

    path("simple-filter", SimpleFilter, name="simple-filter"),
    path("advance-filter", AdvanceFilter, name="advance-filter"),

    path("filter-simple-stocks",
         FilterSimpleStocks, name="filter-simple-stocks")

]
