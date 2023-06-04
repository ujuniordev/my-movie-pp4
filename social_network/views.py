
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse
from .models import Post, Profile
from social_network.forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def dashboard(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('social_network:dashboard')

    followed_posts = Post.objects.filter(
        author__profile__in=request.user.profile.friends.all()
    ).order_by('-created_on')

    return render(
        request, 'dashboard.html', {'form': form, 'posts': followed_posts},
        )


@login_required
def post_update(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('post_update.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))


def register(request):
    if request.method == 'GET':
        return render(
            request, 'registration/register.html',
            {'form': CustomUserCreationForm()}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('social_network:dashboard'))


@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(
        request, 'my_movie/profile_list.html', {'profiles': profiles})


@login_required
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.friends.add(profile)
        elif action == 'unfollow':
            current_user_profile.friends.remove(profile)
        current_user_profile.save()
    return render(request, 'my_movie/profile.html', {'profile': profile})


class PostDetail(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request, 'post_detail.html',
            {
                'post': post,
            },
        )



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_delete.html'
