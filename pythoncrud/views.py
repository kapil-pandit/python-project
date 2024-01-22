from django.http import HttpResponse
from django.shortcuts import render


def homdePage(request):
    data={
        'title':'Kapil',
        'bdata':"Welcome",
        'clist':["PHP", "JS", "C++"],
        'numbers':[12,16,6,65,65,65,65,6,56],
        'students':[
            {
            'name':"Ram",
            'phone':1234567890
            },
            {
            'name':"Ram",
            'phone':1234567890
            }
        ]
    },

    return render(request, 'index.html')
def aboutus(request):
    return HttpResponse("<h1>Welcome to about us page</h1>")
def conatctus(request):
    return HttpResponse("<h1>Welcome to conact us page</h1>")
def updates(request):
    return HttpResponse("<h1>Welcome to update us page</h1>")
def dynamicRoute(request, id):
    return HttpResponse(id, "<h1>Welcome to dynamic Route page</h1>")