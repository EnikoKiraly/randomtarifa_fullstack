from django.shortcuts import render




def index(request):
    
    return render(request, 'random_category/index.html')