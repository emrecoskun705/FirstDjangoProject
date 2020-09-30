from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView
from .models import Column
from .forms import ColumnForm, PostForm

class HomePageView(ListView):
    context_object_name = 'column_list'
    queryset = Column.objects.all()
    template_name='home.html'


class ColumnFormView(FormView):
    template_name = 'column_form.html'
    form_class = ColumnForm
    success_url = '/'

    def form_valid(self, form):
        
        column = form.save(commit=False)
        column.coordinator = self.request.user
        column.save()

        return super().form_valid(form)
        
class PostFormView(FormView):
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
    