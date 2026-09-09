from django.contrib import admin

from .models import Admin, Author, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "problems_solved", "total_points", "authorDetails", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-total_points", "name")


@admin.register(Admin)
class PlatformAdminAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "problems_added"
    )
    search_fields = ("name", "user__name")
    autocomplete_fields = ("user",)
    readonly_fields = ("created_at",)
