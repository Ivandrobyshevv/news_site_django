from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from users.models import User, Likes
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


class AddLikeView(View):
    """Добавление лайков к посту"""

    def post(self, request):
        news_id = int(request.POST.get("news_id"))
        user_id = int(request.POST.get("user_id"))
        url_form = request.POST.get('url_form')

        user = User.objects.get(id=user_id)
        news = News.objects.get(id=news_id)
        try:
            news_like = Likes.objects.get(news=news, user=user)
        except Exception as e:
            news_like = Likes(news=news, user=user, likes=True)
            news_like.save()

        return redirect(url_form)


class RemoveLikeView(View):
    """Удаление лайков к посту"""

    def post(self, request):
        news_like_id = int(request.POST.get("news_likes_id"))
        url_form = request.POST.get('url_form')

        news_like = Likes.objects.get(id=news_like_id)
        news_like.delete()
        return redirect(url_form)
