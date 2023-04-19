from django.contrib import admin
from .models import Profile, Post
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User, Group


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'email')
    fields = ['username', 'email']
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    summernote_fields = ('content')
