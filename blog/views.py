from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/template/blog/post_list.html', {})
