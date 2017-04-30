from django.shortcuts import render
from  website.models import Article,Video
from django.views.generic import ListView, DetailView
# Create your views here.

class ArticleList(ListView):

    model = Article



class ArticleDetail(DetailView):
    model=Article




# def videos(request):
#     context={}
#     context["videos"]=Video.objects.all()
#     return render(request, 'video_list.html', context)


class VideoeList(ListView):
    model=Video
    paginate_by = 1




class VideoeDetail(DetailView):
    model=Video






