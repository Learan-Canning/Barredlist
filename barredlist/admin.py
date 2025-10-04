from django.contrib import admin
from .models import Post, Comment, Reaction
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status',)
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)






# Register your models here.
admin.site.register(Comment)

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reaction_type', 'created_on')
    list_filter = ('reaction_type', 'created_on')
    search_fields = ('user__username', 'post__title')
