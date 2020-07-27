from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.template import loader
from django.forms import TextInput

from .models import Idea, Tag


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/idea_index.html'
    context_object_name = 'idea_list'

    def get_queryset(self):
        """Return all ideas of the user ordered by date"""
        return Idea.objects.filter(owner=self.request.user).order_by('-update_date')


# Idea views
class IdeaDetail(LoginRequiredMixin, generic.DetailView):
    model = Idea
    template_name = 'app/idea_detail.html'


class IdeaCreate(LoginRequiredMixin, CreateView):
    template_name = 'app/idea_form.html'
    model = Idea
    # TODO: allow creating an idea without adding any tags
    fields = ['title', 'description', 'tags', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class IdeaUpdate(LoginRequiredMixin, UpdateView):
    model = Idea
    fields = ['title', 'description', 'tags', 'image']


class IdeaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'app/idea_delete.html'
    model = Idea
    success_url = reverse_lazy('app:index')


# Tag views
class TagIndex(LoginRequiredMixin, generic.ListView):
    template_name = 'app/tag_index.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user).order_by('name')


class TagDetail(LoginRequiredMixin, generic.DetailView):
    model = Tag
    template_name = 'app/tag_detail.html'


class TagCreate(LoginRequiredMixin, CreateView):
    template_name = 'app/tag_form.html'
    model = Tag
    fields = ['name', 'description', 'color']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'description', 'color']

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['name'].widget = TextInput(attrs={})
    #     return form


class TagDelete(LoginRequiredMixin, DeleteView):
    template_name = 'app/tag_delete.html'
    model = Tag
    success_url = reverse_lazy('app:tag-index')
