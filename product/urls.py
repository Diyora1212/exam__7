from .views import home, explore, detail_view, create_view, author_view, login_view, register_view, logout_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('explore/', explore, name='explore'),
    path('detail/', detail_view, name='detail'),
    path('create/', create_view, name='create'),
    path('author/', author_view, name='author'),
    # path('like_author/<int:author_id>/', like_author, name='like_author'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]
