from django.core import validators
from django.db import models

# Create your models here.
from django.db import models
from django.db.models import CASCADE


class User(models.Model):
    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField(max_length=20)
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    age = models.IntegerField()
    gender = models.IntegerField(choices=SEX_CHOICES)
    identityTitle = models.CharField(max_length=10, default=None)
    autograph = models.TextField(max_length=100, default=None)
    school = models.CharField(max_length=20, default=None)
    occupation = models.CharField(max_length=10, default=None)

    class Meta:
        db_table = "UserInfo"


class Tag(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=10, primary_key=True, unique=True)

    class Meta:
        db_table = "Tag"


class Post(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    title = models.IntegerField()
    creatTime = models.DateTimeField()
    hit = models.IntegerField()
    tag = models.ForeignKey(to=Tag, to_field='id', on_delete=CASCADE)
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PostInfo"


class PostSource(models.Model):
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE)
    url = models.URLField(max_length=200)
    imgName = models.CharField(max_length=100)
    imgFile = models.ImageField(upload_to='post/img')
    video = models.URLField(max_length=200)

    class Meta:
        db_table = "postSource"


class Comment(models.Model):
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE)
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE)
    text = models.TextField(max_length=200)
    toUser = models.CharField(max_length=10)
    creatTime = models.DateTimeField()

    class Meta:
        db_table = "comment"


class CommentSource(models.Model):
    comment = models.ForeignKey(to=Comment, on_delete=CASCADE)
    url = models.URLField(max_length=200)
    imgName = models.CharField(max_length=100)
    imgFile = models.ImageField(upload_to='comment/img')

    class Meta:
        db_table = "commentSource"


class Collection(models.Model):
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE)
    creatTime = models.DateTimeField()

    class Meta:
        db_table = "Collection"
