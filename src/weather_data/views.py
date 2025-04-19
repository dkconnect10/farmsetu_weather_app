from django.http import HttpResponse

def home(request):
    return HttpResponse("Weather app is connected!")