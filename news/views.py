from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from users.models import User
from .models import Categories, News


class NewsListView(ListView):
    """Все новости"""
    model = News
    queryset = News.objects.filter(is_published=False)


class NewsDitailView(DetailView):
    """Подробное описание новости"""
    model = News
    queryset = News.objects.filter(is_published=False)


class CategoryViewList(DetailView):
    """Новости по категориям"""
    model = Categories
    template_name = 'news/category.html'


class Search(ListView):
    """Поиск фильма"""

    def get_queryset(self):
        q = self.request.GET.get('q').capitalize()
        return News.objects.filter(
            Q(title__icontains=q) | Q(category__name__icontains=q))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class RemoveOrAddNews(View):
    """Удаление и добавление новостей в заметки"""

    def get_slug_news(self, request):
        news_slug = News.objects.get(id=request.POST.get('news_id')).slug
        return news_slug

    def get_user(self, request):
        return User.objects.get(id=request.user.id)

    def post(self, request):
        if 'remove' in request.POST:
            user = self.get_user(request)
            user.interests.remove(request.POST.get('news_id'))
            return HttpResponseRedirect(reverse('news_detail', args=[self.get_slug_news(request)]))
        else:
            user = self.get_user(request)
            user.interests.add(request.POST.get('news_id'))
            return HttpResponseRedirect(reverse('news_detail', args=[self.get_slug_news(request)]))