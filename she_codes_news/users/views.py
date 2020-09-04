from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory
# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/CreateAccount.html'

class UserAccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/view-profile.html'
    context_object_name = 'user'

    def user_id(self):
        return user.objects.all()

class AuthorView(generic.ListView):
    template_name = 'users/author-detail.html'
    model = NewsStory
    context_object_name = 'story'

    def __str__(self):
        return self.username

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['pk']
        context['author_stories'] = NewsStory.objects.filter(author=username)
        return context

    # def get_author_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     username = self.kwargs['pk']
    #     context['author_details'] = NewsStory.objects.filter(author=username)
    #     return context