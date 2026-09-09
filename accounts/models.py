from django.db import models


class User(models.Model):
    """Platform competitor,solves problems and earns points."""

    name = models.CharField(max_length=150)
    problems_solved = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    authorDetails = models.JSONField(default=dict, blank=True)
    class Meta:
        ordering = ["-total_points", "name"]

    def __str__(self):
        return self.name

class Admin(models.Model):
    """Staff who approve authors and verify problems."""

    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    """User approved to add problems; admins approve applications."""

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="author_profile",
    )
    name = models.CharField(max_length=150)
    problems_added = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
