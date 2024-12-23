from http.client import HTTPResponse
import random

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UsersCreationForm, UsersAuthenticationForm, RecipeForm
from .models import Recipe


def main_index(request: HttpRequest):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, 'recipesapp/main_index.html', {'recipes': random_recipes})


def user_logout(request):
    logout(request)
    return redirect('recipesapp:index')

def registration(request:HttpRequest):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('recipesapp:index')
    else:
        form = UsersCreationForm()
    return render(request,'recipesapp/registration.html',{'form':form})

def user_login(request:HttpRequest):
    if request.method == 'POST':
        form = UsersAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipesapp:index')
    else:
        form = UsersAuthenticationForm
    return render(request, 'recipesapp/login.html', {'form': form})

@login_required(login_url='/login/')
def add_recipe(request:HttpRequest)->HTTPResponse:
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            if not form.cleaned_data['image']:
                recipe.image = 'recipes_photo/default.png'
            recipe.author = request.user.username
            recipe.save()
            return redirect('recipesapp:detail_recipe',pk=recipe.pk)

    else:
        form = RecipeForm()
    return render(request, 'recipesapp/add_recipe.html',{'form':form})


def detail_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipesapp/detail_recipe.html',
                  {'recipe': recipe})

@login_required(login_url='/login/')
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            if not form.cleaned_data['image']:
                recipe.image = 'recipes_photo/default.png'
            recipe.save()
            return redirect('recipesapp:detail_recipe', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipesapp/edit_recipe.html', {'form': form, 'recipe': recipe})
