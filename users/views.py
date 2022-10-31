from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from news.models import Categories, News
from .models import User
from .forms import LoginForm, RegisterForm


# Create your views here.

def logout(request):
    """Выход"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


class UserLoginView(LoginView):
    """Авторизация"""
    template_name = 'users/login.html'
    authentication_form = LoginForm


class UserAccountView(DetailView):
    """Аккаунт"""
    template_name = 'users/account.html'

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)


class UserCreateView(CreateView):
    """Регистрация"""
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    """Редактирование информации"""
    model = User
    fields = ['email', 'username', 'first_name', 'last_name']
    template_name = 'users/account_create.html'
    success_url = reverse_lazy('account')

    def get_form(self, *args, **kwargs):
        form = super(UserUpdateView, self).get_form(*args, **kwargs)
        form.fields["email"].widget.attrs["class"] = "form-control"
        form.fields["username"].widget.attrs["class"] = "form-control"
        form.fields["first_name"].widget.attrs["class"] = "form-control"
        form.fields["last_name"].widget.attrs["class"] = "form-control"
        return form

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)


class InterestsListView(ListView):
    """Интересы"""
    template_name = 'users/interests.html'

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset.interests.all()

    def get_context_data(self, **kwargs):
        context = super(InterestsListView, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


class RemoveNewsAccount(View):
    """Удаление записи"""

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        user.interests.remove(request.POST.get('news_id'))
        return HttpResponseRedirect(reverse('interests'))


class FilterNewsInterestsTView(ListView):
    """Фильтрует новости в заметках"""
    template_name = 'users/interests.html'

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset.interests.filter(category_id__in=self.request.GET.getlist("category"))

    def get_context_data(self, **kwargs):
        context = super(FilterNewsInterestsTView, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context
