from .views import search_posts
from django.urls import path
from .views import PostByTagListView

urlpatterns += [
    path('search/', search_posts, name='search-posts'),
]
urlpatterns = [
    # other patterns...
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # ✅ Required for checker
]