from django.http import HttpResponse

def index(request):
    return HttpResponse('Aqui va a estar la pagina de pedidos')