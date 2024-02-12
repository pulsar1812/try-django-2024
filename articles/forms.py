from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f"\"{title}\" is already in use. Please pick another title.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # Dictionary
    #     print('cleaned_data:', cleaned_data)
    #     title = cleaned_data.get('title')
    #     print('title:', title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data:', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title is not None and title.lower().strip() == 'the office':
            self.add_error('title', 'This title is taken.')     # Field error
            # raise forms.ValidationError('This title is taken.')   # Errors of the whole form
        return cleaned_data