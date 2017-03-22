from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Comment, Opinion
from .forms import CommentForm, OpinionForm


class CommentsFormView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments-form.html'
    success_url = reverse_lazy('storedxss:comments-list')

    def get_context_data(self, **kwargs):
        context = super(CommentsFormView, self).get_context_data(**kwargs)
        context['opinions'] = Opinion.objects.all()[:3]
        return context


class CommentsListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comments-list.html'


class OpinionCreateView(CreateView):
    model = Opinion
    form_class = OpinionForm
    template_name = 'opinion-form.html'
    success_url = reverse_lazy('storedxss:comments-create')
