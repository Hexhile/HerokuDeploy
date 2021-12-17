from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
 
from .models import Post

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def resultados(request, post_id):
    response = "Estas viendo el post # %s."
    return HttpResponse(response % post_id)

def likes(request, post_id):
    return HttpResponse("Te gusta %s." % post_id)