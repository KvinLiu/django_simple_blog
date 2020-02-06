from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# QuerySet Basics with shell python manage.py shell
# from posts.models import Post
# Post.objects.all()
# Post.objects.get(id="...")
# Post.objects.filter(title_icontains="...")
# Post.objects.create(title="...", context="...")

# import Forms
from .forms import PostForm

# import Models
from .models import Post

# the logic handle the request the browser/client make
def post_create(request):
    # form = PostForm()
    form = PostForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        # message success
        messages.success(
            request, "<a href='#'>Successfully</a> Created", extra_tags="html_safe"
        )
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.success(request, "Not Successfully Created")

    # if request.method == "POST":
    #     print(request.POST.get("title"))
    #     print(request.POST.get("context"))
    #     Post.objects.create(title=...)

    # return HttpResponse("<h1>Create</h1>")
    return render(request, "post_form.html", context)


def post_detail(request, id):
    # instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    context = {"title": instance.title, "instance": instance}
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {"object_list": queryset, "title": "List"}
    # if request.user.is_authenticated:
    #     context = {"title": "My User List"}
    # else:
    #     context = {"title": "List"}
    # return HttpResponse("<h1>List</h1>")
    return render(request, "index.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {"title": instance.title, "instance": instance, "form": form}
    return render(request, "post_form.html", context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
