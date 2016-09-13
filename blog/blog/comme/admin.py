from django.contrib import admin
from .models import Commentario

class CommentarioModelAdmin(admin.ModelAdmin):
    list_display = ["commfield", "pubdate"]

    class Meta:
        model = Commentario

admin.site.register(Commentario, CommentarioModelAdmin)
# Register your models here.
