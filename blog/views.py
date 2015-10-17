from django.shortcuts import render
import datetime
from .models import Post
from django.utils import timezone

def post_list(request):
	right_now = datetime.datetime.now()
	posts = Post.objects.exclude(published_date = None).filter(published_date__lte=timezone.now).order_by("-published_date")
	return render(request, "index.html", {"time": right_now, "posts": posts})
