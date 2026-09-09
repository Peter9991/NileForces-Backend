from django.db import models


class User(models.Model):
    """Platform competitor,solves problems and earns points."""

    name = models.CharField(max_length=150)
    problems_solved = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    authorDetails = models.jsonField(default=dict)
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

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    user = models.OneToOneField(
        User,
        on_delete=models.set_null,
        related_name="author_profile",
    )
    name = models.CharField(max_length=150)
    problems_added = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text="Admin must approve before this author can publish.",
    )
    reviewed_by = models.ForeignKey(
        Admin,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_authors",
        help_text="Admin who approved or rejected this author.",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.status})"
