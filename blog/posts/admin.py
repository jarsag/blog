from django.contrib import admin

from .models import Post, Commentario


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
	    model = Post

class CommentarioModelAdmin(admin.ModelAdmin):
    list_display = ["commfield", "pubdate"]

    class Meta:
        model = Commentario

admin.site.register(Commentario, CommentarioModelAdmin)


admin.site.register(Post, PostModelAdmin)

# Register your models here.
