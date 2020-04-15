from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# DRY = DONT REPEAT YOURSELF

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    qs = BlogPost.objects.all()[:5]
    print(qs)
    context = {"title": "Welcome to Try Django", 'blog_list': qs}
    tempalete_name = "home.html"
    return render(request, tempalete_name, context)



def about_page(request):
    return render(request, "hello_world.html", {"title":"About us"})



def contact_page(request):
	print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		"title":"Contact us",
		"form":form
	}

	return render(request, "form.html", context)
    


def exapmle_page(request):
	return render(request, "hello_world.html", {"title":"Contact us"})
    