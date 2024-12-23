from django.urls import path

from .views import main_index, registration, user_logout, user_login, add_recipe, edit_recipe, detail_recipe

app_name = 'recipesapp'

urlpatterns =[
    path("", main_index, name='index'),
    path("registration/", registration, name='registration'),
    path('logout/', user_logout, name='user_logout'),
    path('login/', user_login, name='user_login'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/edit/', edit_recipe, name='edit_recipe'),
    path('recipe/<int:pk>/', detail_recipe, name='detail_recipe'),
]