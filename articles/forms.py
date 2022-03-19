from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    FORBIDDEN_TITLES = ('admin', 'login', 'logout')

    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if any(map(lambda a, b: a == b, [title.lower().strip()] * len(self.FORBIDDEN_TITLES), self.FORBIDDEN_TITLES)):
            self.add_error('title', 'This title cannot be used.')
        if qs.exists():
            self.add_error('title', f'\"{title}\" This title already exists. Please, pick another title.')
        return data


class ArticleFormOld(forms.Form):
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