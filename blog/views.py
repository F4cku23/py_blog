from django.shortcuts import render

# Create your views here.
def render_aticles(request):
    return render(request, 'articles.html')