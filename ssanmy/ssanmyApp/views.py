from django.shortcuts import render
from .models import Post

def index(request):
    mods_list = Post.objects.order_by('-post_title')
    context = {'mods_list': mods_list}
    return render(request, 'ssanmyApp/main_detail.html', context)

# Create your views here.
