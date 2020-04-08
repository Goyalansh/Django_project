from django.shortcuts import render

# Create your views here.

def index(request):
    """the home page for learning"""
    return render(request, 'learning_logs/index.html')
