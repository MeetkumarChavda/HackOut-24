from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # If this migration depends on any other migrations, list them here
        # Example: ('your_app_name', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
