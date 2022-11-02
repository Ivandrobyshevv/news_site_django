from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from news.models import Categories
from .models import User, Newsletter
from .forms import LoginForm, RegisterForm, UpdateUserForm
from .service import send


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
    form_class = UpdateUserForm
    template_name = 'users/account_create.html'
    success_url = reverse_lazy('account')

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


class NewsletterView(View):
    def post(self, request):
        user = User.objects.get(id=request.user.id)
        category_list = request.POST.getlist("category")
        _, user_bool = Newsletter.objects.update_or_create(user=user)
        if not user_bool:
            _.categories.set(category_list)
        else:
            send(user=user, categories_id=category_list)
            for category in category_list:
                _.categories.add(int(category))
        return redirect('account')
