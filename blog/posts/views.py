from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Commentario
from .forms import PostForm,CommentarioForm
from django.contrib import messages

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
	instance = form.save(commit=False)
	instance.save()
	# messages.success(request, "Created")
	return HttpResponseRedirect(instance.get_absolute_url())
    # else:
	# messages.error(request, "Not Created")
    context = {
	    "form": form,
	}
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
    	"title": post.title,
    	"post": post,
        "comments": post.comments.all(),
        "form": CommentarioForm(request.POST or None)}
    
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
	# messages.success(request, "Saved")
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
    # messages.success(request, "Deleted")
    return redirect("posts:list")

def api_post_delete(request):
    post = get_object_or_404(Post, id=int(request.GET['post_id']))
    post.delete()

    return HttpResponse('Ok')


def api_comm_delete(request):
    comment = get_object_or_404(Commentario, id=int(request.GET['comm_id']))
    comment.delete()

    return HttpResponse('Ok')


# def api_comm_delete(request):
#     comm = get_object_or_404 (Commentario, pk=int(request.GET['comm_id']))
#     comm.delete()

    # return HttpResponse('Ok')

def comm_delete(request, id, pk=None):
    comme = get_object_or_404(Commentario, pk=pk)
    comme.delete()
    # messages.success(request, "Deleted")
    return redirect("posts:list")


def comm_create(request, id=None):
    post = get_object_or_404(Post, id=id)
    
    form = CommentarioForm(request.POST or None)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = post
        comment.save()
        
        # messages.success(request, "Created")
        
        return HttpResponseRedirect(post.get_absolute_url())
    # else:
    #     messages.error(request, "Not Created")
    
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