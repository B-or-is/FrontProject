from django.shortcuts import render

# Create your views here.


def plug_graphql(request):
    return render(request, 'plug_graphgl.html')
