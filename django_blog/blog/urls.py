from .views import search_posts

urlpatterns += [
    path('search/', search_posts, name='search-posts'),
]
