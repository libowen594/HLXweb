# Generated by Django 3.2.3 on 2021-05-31 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('toUser', models.CharField(max_length=10)),
                ('creatTime', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('title', models.IntegerField()),
                ('creatTime', models.DateTimeField()),
                ('hit', models.IntegerField()),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'PostInfo',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')])),
                ('identityTitle', models.CharField(default=None, max_length=10)),
                ('autograph', models.TextField(default=None, max_length=100)),
                ('school', models.CharField(default=None, max_length=20)),
                ('occupation', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='PostSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('imgName', models.CharField(max_length=100)),
                ('imgFile', models.ImageField(upload_to='post/img')),
                ('video', models.URLField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.post')),
            ],
            options={
                'db_table': 'postSource',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.user'),
        ),
        migrations.CreateModel(
            name='CommentSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('imgName', models.CharField(max_length=100)),
                ('imgFile', models.ImageField(upload_to='comment/img')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.comment')),
            ],
            options={
                'db_table': 'commentSource',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.user'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatTime', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hlx.user')),
            ],
            options={
                'db_table': 'Collection',
            },
        ),
    ]