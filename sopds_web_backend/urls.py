from django.urls import re_path, path
from sopds_web_backend import views

app_name = 'opds_web_backend'

urlpatterns = [
    re_path(r'^search/books/$', views.SearchBooksView, name='searchbooks'),
    re_path(r'^search/authors/$', views.SearchAuthorsView, name='searchauthors'),
    re_path(r'^search/series/$', views.SearchSeriesView, name='searchseries'),
    path('catalog/', views.CatalogsView, name='catalog'),
    path('book/', views.BooksView, name='book'),
    path('author/', views.AuthorsView, name='author'),
    path('genre/', views.GenresView, name='genre'),
    path('series/', views.SeriesView, name='series'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('bs/delete/', views.BSDelView, name='bsdel'),
    path('bs/clear/', views.BSClearView, name='bsclear'),
    path('', views.hello, name='main'),
]

# handler403 = 'views.handler403'