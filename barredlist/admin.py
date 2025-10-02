from django.contrib import admin
from .models import Post, Comment, Reaction

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reaction_type', 'created_on')
    list_filter = ('reaction_type', 'created_on')
    search_fields = ('user__username', 'post__title')
