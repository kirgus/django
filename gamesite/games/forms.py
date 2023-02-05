from django import forms

from .models import Game, Category


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']
        labels = {'name': ''}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}
