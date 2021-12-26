from django.shortcuts import render
from .models import Random_Category, Random_Detail, Quote
import random



def index(request):
    categorys = Random_Category.objects.all()
    details = Random_Detail.objects.order_by('category','?').distinct('category') #shuffle and one of each category
    
     
    total_random_query = Random_Detail.objects.order_by('?')
    random_number = random.randint(0, len(total_random_query)-1) 
    total_random_detail = total_random_query[random_number]
    print(total_random_detail)

    quote_random = Quote.objects.order_by('?')
    random_quote_number = random.randint(0, len(quote_random)-1) 
    quote = quote_random[random_quote_number]
    
    context = {
    'categorys':categorys, 
    'details':details,
    'total_random_detail':total_random_detail ,
    'quote': quote
    
    }

    return render(request, 'random_category/index.html',context )