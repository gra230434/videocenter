from django.shortcuts import render


# Create your views here.
def index(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Hello, world. You're at the video index."
    context = {'mes': message}
    return render(request, 'index/index.html', context)
