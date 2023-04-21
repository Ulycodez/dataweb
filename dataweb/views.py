from django.shortcuts import render

# Create your views here.
def dataweb(request):
    return render(request, 'dataweb/dataweb.html', {})