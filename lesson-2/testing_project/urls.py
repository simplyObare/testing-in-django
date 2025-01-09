from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("products/", views.products, name="products"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
]
