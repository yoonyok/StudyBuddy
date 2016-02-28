from django.contrib import admin

# Register your models here.
# see https://docs.djangoproject.com/en/1.9/ref/contrib/admin/ for more admin options
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["title", "updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["content", "title"]
    readonly_fields = ["timestamp", "updated", "slug", "lat", "lon"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)