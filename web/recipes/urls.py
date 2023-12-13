from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/result/<str:label>/', views.recipe_view, name='result'),
    path('recipe/<str:meal_id>/', views.recipe_detail_view, name="recipe_detail"),

]

