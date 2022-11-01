from django.urls import path
from . import views

urlpatterns = [
    path("category/<slug:slug>/", views.CategoryViewList.as_view(), name='category'),
    path("news/<slug:slug>/", views.NewsDitailView.as_view(), name='news_detail'),
    path("search/", views.Search.as_view(), name="search"),
    path("add-likes/", views.AddLikeView.as_view(), name='add-likes'),
    path("remove-likes/", views.RemoveLikeView.as_view(), name='remove-likes'),
    path('remove-or-add/', views.RemoveOrAddNews.as_view(), name="remove-or-add"),
    path("", views.NewsListView.as_view(), name='homepage'),

]


