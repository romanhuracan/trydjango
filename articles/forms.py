from django import forms

from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())

    def clean_title(self):
        title = self.cleaned_data.get('title')
        reserved = ('admin', 'login', 'logout')
        if any(map(lambda a, b: a == b, [title.lower().strip()] * len(reserved), reserved)):
            raise forms.ValidationError('This title cannot be used.')
        if Article.objects.filter(title=title):
            raise forms.ValidationError('The same title already exists.')
        return title