from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from urllib.parse import quote_plus

# Create your views here.

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
    form = PostForm(request.POST or None, request.FILES or None)
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


def post_detail(request, slug):
    # instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, slug=slug)
    share_str = quote_plus(instance.context)
    context = {"title": instance.title, "instance": instance, "share_string": share_str}
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()  # .order_by("-timestamp")
    paginator = Paginator(queryset, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)

    context = {
        "object_list": contact,
        "title": "List",
        "page_request_var": page_request_var,
    }
    # if request.user.is_authenticated:
    #     context = {"title": "My User List"}
    # else:
    #     context = {"title": "List"}
    # return HttpResponse("<h1>List</h1>")
    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {"title": instance.title, "instance": instance, "form": form}
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("posts:list")
