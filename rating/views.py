from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import SimpleForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Rating
#
#

class RatingsDetailView(DetailView):
    model = Rating

class RatingListView(ListView):
    #model = Rating

    #context_object_name = 'rating_objects' 
    #или
    queryset = Rating.objects.all()
    context_object_name = 'rating_objects'

    #def get_context_data(self, **kwargs):
    #    context =  super().get_context_data(**kwargs)
    #    context['extra_context'] = 'Foo'
    #    return context

class RatingEntryListView(ListView):
    template_name = 'rating/rating_by_name.html'
    context_object_name = 'rating_name_objects'

    def get_queryset(self):
        return Rating.objects.filter(name=self.kwargs['name'])

    



#@method_decorator(login_required)
class SimpleView(View):
    name = 'Anonymous'

    def get(self, request):
        return HttpResponse(f'Hello, {self.name}')

class Foo(SimpleView):
    name = 'Foo'

class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'initial value'}
    template_name = 'form.templates.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        return render(request, self.template_name, {'form': form})