"""Posts views."""

# Django
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# views
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class ListPostView(LoginRequiredMixin, ListView):
    """Return all post"""

    template_name = 'posts/feed.html'
    model = Post
    paginate_by = 30
    ordering = ('-created')
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new Post"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """ Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
