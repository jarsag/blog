from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Commentario
from .forms import CommentarioForm
from django.contrib import messages
from django.shortcuts import render

def comm_create(request):
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


    return render(request, "comm_detail.html", context)
# Create your views here.
