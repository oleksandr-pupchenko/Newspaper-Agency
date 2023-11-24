from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
