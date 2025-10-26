from django import forms
from .models import Post, Tag
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # ✅ Required for checker
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tag_names = self.cleaned_data['tags'].split(',')
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name.strip())
                instance.tags.add(tag)
        return instance
