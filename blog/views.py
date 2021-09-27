from django.shortcuts import render
from .models import blogModel

# Create your views here.
def blog(request):
    blogs = blogModel.objects.all()
    context = {
        "blogpost": blogs,
    }
    return render(request, 'blog.html', context)
