from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Recipe, Users


class UsersCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'field-forms', 'placeholder': 'User Name'})
                               )
    password1 = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'field-forms', 'placeholder': 'User password'})
                                )
    password2 = forms.CharField(required=True, label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'field-forms', 'placeholder': 'User password'})
                                )



class UsersAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required=True, label='Логин', widget=forms.TextInput(
        attrs={'class': 'field-forms', 'placeholder': 'User Name'})
                               )
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'field-forms', 'placeholder': 'User password'})
                               )
    class Meta:
        model = Users


class RecipeForm(forms.ModelForm):
    name = forms.CharField(required=True, label='', max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'recipe-name', 'placeholder': 'Название рецепта',
                                             'size':'30'}))
    description = forms.CharField(required=True, label='', max_length=200,
                                  widget=forms.Textarea(
                                      attrs={'class': 'no-resize', 'placeholder': 'Описание рецепта'}))
    steps = forms.CharField(required=True, label='',
                                    widget=forms.Textarea(
                                        attrs={'class': 'no-resize',  'placeholder': 'Пошаговая инструкция'}))
    cooking_time = forms.IntegerField(required=True, label='Время приготовления (мин.)', min_value=5, max_value=500,
                              widget=forms.NumberInput(
                                  attrs={'class': 'field-forms','size':'6'}))
    image = forms.ImageField(required=False, label='',
                             widget=forms.FileInput(
                                 attrs={'placeholder': 'Изображение рецепта', 'class': 'field-forms'}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'cooking_time', 'image']