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


# landing page redirects to idea index if logged in and to about otherwise
def redirect_landing_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:index'))
    else:
        return HttpResponseRedirect(reverse('app:about'))

# check off milestones of an idea
# def complete_milestone(request):
#     """Complete milestone and set completion date"""
#     if request.user.is_authenticated:
#
#     form.instance.completed = True
#     form.instance.completed_date = timezone.now
#
# def uncomplete_milestone(self, form):
#     """Revert completion"""
#     form.instance.completed = False
#     form.instance.completed_date = None


# Idea views
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'app/idea_index.html'
    context_object_name = 'idea_list'

    def get_queryset(self):
        """Return all ideas of the user ordered by date"""
        return Idea.objects.filter(owner=self.request.user).order_by('-update_date')

class IdeaDetail(LoginRequiredMixin, generic.DetailView):
    model = Idea
    template_name = 'app/idea_detail.html'

class IdeaCreate(LoginRequiredMixin, CreateView):
    template_name = 'app/idea_form.html'
    model = Idea
    # TODO: allow creating an idea without adding any tags
    fields = ['title', 'description', 'tags']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class IdeaUpdate(LoginRequiredMixin, UpdateView):
    model = Idea
    fields = ['title', 'description', 'tags']


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
