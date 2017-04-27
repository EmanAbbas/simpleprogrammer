from django.shortcuts import render
from  website.models import Article
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    context={}
    context["articles"]=Article.objects.all()
    return render(request, 'index.html', context)


class ArticleDetail(DetailView):
    model=Article
    template_name = 'article.html'



