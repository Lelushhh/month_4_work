from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog

def search_view(request):
     query = request.GET.get('s', '')
     if query:
         blog = Blog.objects.filter(name_blog__icontains=query)
     else:
         blog = Blog.objects.none
     return render(
         request,
         template_name='blog/blog_list.html',
         context={
             'blog': blog
         } 
     )






def blog(request):
    if request.method == "GET":
        blog = Blog.objects.all()
    return render(
        request,
        template_name='blog/blog_list.html',
        context={
            'blog':blog
        }
    )

def blog_detail(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(Blog, id=id)
    return render(
        request,
        template_name='blog/blog_detail.html',
        context={
            'blog_id': blog_id
        }
    )

def first_blog(request):
    if request.method == 'GET':
        return HttpResponse("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    
def second_blog(request):
    if request.method == 'GET':
        return HttpResponse("Lorem Ipsum")
    
def third_blog(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://images.unsplash.com/photo-1517960413843-0aee8e2b3285?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGlmZXxlbnwwfHwwfHx8MA%3D%3D">')
    