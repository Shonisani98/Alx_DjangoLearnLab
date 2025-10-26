from django.db.models import Q
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from taggit.models import Tag

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug)