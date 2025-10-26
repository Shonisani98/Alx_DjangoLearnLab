from .views import search_posts, posts_by_tag

urlpatterns += [
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
]
def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})
