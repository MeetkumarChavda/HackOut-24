from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', '0002_create_user_profile_model_for_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_auth_id',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='social_auth_provider',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
