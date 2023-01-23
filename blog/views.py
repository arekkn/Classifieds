from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post, Comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.forms import CommentForm, PostForm


def post(request, pk):
    that_post = Post.objects.get(id=pk)
    list_of_comments = Comment.objects.filter(post_id=pk)
    list_of_places = that_post.places.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = that_post
            obj.author = request.user
            obj.save()

            return redirect('post', pk=pk)

    form = CommentForm()
    context = {'post': that_post,
               'list_of_comments': list_of_comments,
               'list_of_places': list_of_places,
               'form': form}
    return render(request, 'blog/post.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'list_of_posts'
    ordering = ['-pub_date']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'list_of_posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        that_post = self.get_object()
        if self.request.user == that_post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        that_post = self.get_object()
        if self.request.user == that_post.author:
            return True
        return False
