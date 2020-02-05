from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# QuerySet Basics with shell python manage.py shell
# from posts.models import Post
# Post.objects.all()
# Post.objects.filter(title_icontains="...")
# Post.objects.create(title="...", context="...")

# import Models
from .models import Post

# the logic handle the request the browser/client make
def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request):
    context = {"title": "Detail"}
    return render(request, "index.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {"object_list": queryset, "title": "List"}
    # if request.user.is_authenticated:
    #     context = {"title": "My User List"}
    # else:
    #     context = {"title": "List"}
    # return HttpResponse("<h1>List</h1>")
    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
