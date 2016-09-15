from django.contrib import admin

from .models import Post, Commentario, Prev


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","content","prev", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title","content","prev"]
    class Meta:
	    model = Post

class CommentarioModelAdmin(admin.ModelAdmin):
    list_display = ["commfield", "pubdate", "name"]

    class Meta:
        model = Commentario

class PrevModelAdmin(admin.ModelAdmin):
    list_display = ["prev"]

    class Meta:
        model = Prev


admin.site.register(Commentario, CommentarioModelAdmin)


admin.site.register(Post, PostModelAdmin)

admin.site.register(Prev, PrevModelAdmin)


# Register your models here.
