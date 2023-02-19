from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("<str:product_name>/", views.product_page, name="product_page"),
]
