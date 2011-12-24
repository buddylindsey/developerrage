from django import forms

class ComicForm(forms.Form):
    title = forms.CharField()
    image = forms.ImageField()

