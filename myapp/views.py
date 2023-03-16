from django.shortcuts import render
from myapp.forms import NewsInformation


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def create_view(request):
    form = NewsInformation()

    context = {
        'news_form': form,
    }

    return render(request, 'create_news.html', context)

