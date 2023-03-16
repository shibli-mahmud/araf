from django.contrib.auth.forms import forms
from myapp.models import NewsInformation


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsInformation
        fields = [
            'news_title',
            'news_details',
            'cover_image',
        ]
