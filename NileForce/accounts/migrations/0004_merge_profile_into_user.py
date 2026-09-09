from django.db import migrations, models


def move_profile_data_to_users(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    Profile = apps.get_model("accounts", "Profile")

    for profile in Profile.objects.select_related("user"):
        User.objects.filter(pk=profile.user_id).update(
            display_name=profile.display_name,
            bio=profile.bio,
            avatar_url=profile.avatar_url,
            solved_problems_counter=profile.Solved_Problems_Counter,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_profile_solved_problems_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="display_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="avatar_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="solved_problems_counter",
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(move_profile_data_to_users, migrations.RunPython.noop),
        migrations.DeleteModel(name="Profile"),
    ]
