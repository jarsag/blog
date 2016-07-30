from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm,CommentarioForm
from django.contrib import messages

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
	instance = form.save(commit=False)
	instance.save()
	messages.success(request, "Created")
	return HttpResponseRedirect(instance.get_absolute_url())
    else:
	messages.error(request, "Not Created")
    context = {
	    "form": form,
	}
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
	"title": instance.title,
	"instance":instance,
}
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
	"object_list": queryset,
	"title": "My List"
}

    return render(request, "index.html", context)

def post_updated(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
	instance = form.save(commit=False)
	instance.save()
	messages.success(request, "Saved")
	return HttpResponseRedirect(instance.get_absolute_url())

    context = {
	"title": instance.title,
	"instance": instance,
	"form": form,
}
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")

def comm_create(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = CommentarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Created")
    context = {
	    "form": form,
	}

    return render(request, "comm_form.html", context)

def comm_detail(request, id=None):
    instance = get_object_or_404(Commentario, id=id)
    context = {
               "instance": instance,
    }

    return render(request, "post_detail.html", context)