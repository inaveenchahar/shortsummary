from django.urls import path
from . import views


app_name = 'book'


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('who-and-why/', views.who_why_view, name='who_why'),
    path('suggestion/', views.suggestion_view, name='suggestion'),
    path('add-book/', views.add_book, name='add_book'),
    path('<tag_slug>/', views.tag_details, name='tag_details'),
    path('book/<book_slug>/summary/', views.book_details, name='book_details'),
    path('book/<book_slug>/edit/', views.edit_book, name='edit_book'),
]
