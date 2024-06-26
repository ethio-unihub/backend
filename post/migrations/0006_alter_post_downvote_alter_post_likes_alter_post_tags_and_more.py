# Generated by Django 4.2.11 on 2024-03-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
        ('post', '0005_remove_post_owner_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='downvoted_posts', to='user.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to='user.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='post.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvoted_posts', to='user.profile'),
        ),
    ]
