from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("<h1>Welcome to about us page</h1>")
def conatctus(request):
    return HttpResponse("<h1>Welcome to conact us page</h1>")
def updates(request):
    return HttpResponse("<h1>Welcome to update us page</h1>")