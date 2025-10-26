from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tag_names = self.cleaned_data['tags'].split(',')
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name.strip())
                instance.tags.add(tag)
        return instance
