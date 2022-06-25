from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import blog



# Create your views here.
class PostListView(ListView):
    model=blog
    template_name = "post_list.html"
    
class PostCreateView(CreateView):
    model=blog
    fields=[
    "title","slug","author", "body", "publish", "created", "updated", "status"
    ]
    template_name = "post_form.html"
    success_url="/"

class PostDetailView(DetailView):
    model=blog
    template_name= "post_detail.html"

class PostUpdateView(UpdateView):
    model=blog
    fields=[
    "title","slug","author", "body", "publish", "created", "updated", "status"
    ]
    template_name = "post_detail.html"
    success_url= "/"

class PostDeleteView(UpdateView):
    model=blog
    fields=[
    "title","slug","author", "body", "publish", "created", "updated", "status"
    ]
    template_name = "post_confirm_delete.html"
    success_url= "/"




