
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import PostForm
from django.views import generic
from django.urls import reverse
from .models import Post, Profile
from social_network.forms import CustomUserCreationForm
from django.shortcuts import render, redirect


def dashboard(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')

    followed_posts = Post.objects.filter(
        author__profile__in=request.user.profile.friends.all()
    ).order_by("-created_on")

    return render(
        request, 'dashboard.html', {'form': form, 'posts': followed_posts},
        )


def register(request):
    if request.method == 'GET':
        return render(
            request, 'registration/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('social_network:dashboard'))


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(
        request, 'my_movie/profile_list.html', {'profiles': profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.friends.add(profile)
        elif action == "unfollow":
            current_user_profile.friends.remove(profile)
        current_user_profile.save()
    return render(request, "my_movie/profile.html", {"profile": profile})
