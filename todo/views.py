from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from braces.views import SelectRelatedMixin
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.


class TodoListView(SelectRelatedMixin, ListView):
    model = models.Todo
    select_related = ("user",)


class TodoDetailView(DetailView):
    context_object_name = 'todo_details'
    model = models.Todo
    template_name = 'todo/todo_detail.html'


class TodoCreateView(CreateView):
    fields = ("name",'description','priority','task_type','estimated_time','ETA')
    model = models.Todo

    def form_valid(self, form):
        form.instance.user = self.request.user# success_url = reverse_lazy("project:blcreate")
        
        return super(TodoCreateView, self).form_valid(form)


    def get_form(self, form_class=None):
        form = super(TodoCreateView, self).get_form(form_class)
        # form.fields['ETA'].widget.attrs.update({'class': 'datepicker'})
        return form

class TodoUpdateView(UpdateView):
    fields = ("name",'description','priority','task_type','estimated_time','ETA')
    model = models.Todo


class TodoDeleteView(DeleteView):
    model = models.Todo
    success_url = reverse_lazy("todo:list")


class TodoLogCreate(CreateView):
    model = models.TodoLog
    fields = ['log', 'presentage_complete']
    template_name = 'todo/todolog_form.html'

    def get_initial(self):
        todo_id = self.kwargs['pk']
        todo = get_object_or_404(models.Todo, pk=todo_id)
        return {
            'presentage_complete':todo.presentage_complete,
        }

    def form_valid(self, form):
        todo_id = self.kwargs.pop('pk')
        todo = get_object_or_404(models.Todo, pk=todo_id)
        todo.presentage_complete = form.instance.presentage_complete
        if todo.presentage_complete == 100:
            todo.task_completed = True
        else:
            todo.task_completed = False
        todo.save()
        form.instance.todo = todo
        return super(TodoLogCreate ,self).form_valid(form)


class TodoLogUpdate(UpdateView):
    model = models.TodoLog
    fields = ['log', 'presentage_complete']
    template_name = 'todo/todolog_form.html'

    def form_valid(self, form):
        # todo_id = self.kwargs.pop('pk')

        todo = form.instance.todo
        todo.presentage_complete = form.instance.presentage_complete
        if todo.presentage_complete == 100:
            todo.task_completed = True
        else:
            todo.task_completed = False
        todo.save()
        form.instance.todo = todo
        return super(TodoLogUpdate ,self).form_valid(form)