from django.shortcuts import render
from .models import testPost

def index(request):
    mods_list = testPost.objects.order_by('-test_title')
    context = {'mods_list': mods_list}
    return render(request, 'ssanmyApp/main_detail.html', context)

# Create your views here.
