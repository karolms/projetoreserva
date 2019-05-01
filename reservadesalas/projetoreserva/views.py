from django.shortcuts import render
from .models import Info 
# Create your views here.


def home(request):
	context = {
		'info': Info.objects.all()
	}
	return render (request, 'projetoreserva/home.html', context)


def sobre(request):
	return render (request, 'projetoreserva/sobre.html', {'title': 'sobre'})


