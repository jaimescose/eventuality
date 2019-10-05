from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dictionary = {'inserts_me': "This is the variable value"}
    return render(request,'even/index.html',context=dictionary)
