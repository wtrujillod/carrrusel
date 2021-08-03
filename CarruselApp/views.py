from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    context = RequestContext(request)
    order = OrdenTrabajo.objects.filter(estado=1)
    img_order = []
    context['order'] = order
    context['img_order'] = img_order
    return render(request, 'Home.html', context.flatten())


def carrusel_main(request):
    context = RequestContext(request)
    try:
        _order = request.POST['orden']
        if _order == '':
            img_order = []
            context['img_order'] = img_order
            return render(request, 'carrusel_main.html', context.flatten())

        img_order = ImageOrdenTrabajo.objects.filter(orden=_order)
        context['img_order'] = img_order
    except Exception as e:
        print('{} - Función: {}'.format(e, 'carrusel_main'))
        return HttpResponse(status=500)

    return render(request, 'carrusel_main.html', context.flatten())
