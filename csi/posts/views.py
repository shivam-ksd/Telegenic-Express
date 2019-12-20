from urllib import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q


from .forms import PostForm
from .models import Post

def post_create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Successfully Uploaded")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	share_string=quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string":share_string
	}
	return render(request,"post_detail.html",context)
	#return HttpResponse("<h1>Detail</h1>")

def post_list(request):
	queryset_list =Post.objects.all()#.order_by("-timestamp")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 15) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	#page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset=paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
	}
	return render(request,"post_list.html",context)

	
    
    
	#return HttpResponse("<h1>List</h1>")

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
		}
	#return HttpResponse("<h1>Update</h1>")
	return render(request,"post_form.html",context)


def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect("posts:list")



	#return HttpResponse("<h1>Delete</h1>")