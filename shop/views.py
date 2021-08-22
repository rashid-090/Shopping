from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def home(request,c_slug=None):
    c_page=None
    product=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product=Products.objects.filter(category=c_page,available=True)
    else:
        product=Products.objects.all().filter(available=True)
    categ=Category.objects.all()
    paginator=Paginator(product,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        prod=paginator.page(page)
    except(EmptyPage,InvalidPage):
        prod=paginator.page(paginator.num_pages)        
    return render(request,'index.html',{'pr':product,'ct':categ,'pg':prod})



def ProductDetails(request,c_slug,product_slug):
    try:
        products=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e    
    return render(request,'item.html',{'pr':products})



def Searching(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pr':products})


  