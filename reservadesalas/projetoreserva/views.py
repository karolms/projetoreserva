from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Info 

# Create your views here.


def home(request):
	context = {
		'info': Info.objects.all()
	}
	return render (request, 'projetoreserva/home.html', context)

class InfoListView(ListView):
	model = Info
	template_name = 'projetoreserva/home.html'	
	context_object_name = 'info'
	ordering = ['-date_posted']

class InfoDetailView(DetailView):
	model = Info
	

class InfoCreateView(LoginRequiredMixin, CreateView):
	model = Info
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class InfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Info
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


	def test_func(self):
		info = self.get_object()
		if self.request.user == info.author:
			return True
		return False  


class InfoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Info
	success_url = '/'

	def test_func(self):
		info = self.get_object()
		if self.request.user == info.author:
			return True
		return False




def sobre(request):
	return render (request, 'projetoreserva/sobre.html', {'title': 'sobre'})


