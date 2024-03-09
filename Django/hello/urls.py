from . import views
from django.urls import path
from hello import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

#from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipes"),
    path("check_items", views.checkFood),
    path("about/", views.about, name="about"),
]