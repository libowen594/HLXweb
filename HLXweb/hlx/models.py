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
    id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='id')
    name = models.CharField(max_length=20)
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(choices=SEX_CHOICES, verbose_name='性别')
    identityTitle = models.CharField(max_length=10, default=None, null=True, verbose_name='头衔')
    autograph = models.TextField(max_length=100, default=None, null=True, verbose_name='个性签名')
    school = models.CharField(max_length=20, default=None, null=True, verbose_name='学校名称')
    occupation = models.CharField(max_length=10, default=None, null=True, verbose_name='职业')

    class Meta:
        db_table = "UserInfo"
        verbose_name = '用户信息表'


class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='板块id')
    title = models.CharField(max_length=10, verbose_name='板块名称')
    description = models.CharField(max_length=200, verbose_name='描述信息')

    class Meta:
        db_table = 'Category'
        verbose_name = '板块信息表'


class Tag(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='分类id')
    category = models.ForeignKey(to=Category, to_field='id', on_delete=CASCADE, verbose_name='tag所属板块')
    name = models.CharField(max_length=10, verbose_name='分类名称')

    class Meta:
        db_table = "Tag"
        verbose_name = '帖子分类表'


class Post(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='帖子id')
    category = models.ForeignKey(to=Category, to_field='id', on_delete=CASCADE, verbose_name='帖子所属板块')
    title = models.IntegerField(verbose_name='标题')
    text = models.TextField(max_length=500, verbose_name='帖子内容', default=None, null=True,)
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE, verbose_name='用户id')
    tag = models.ForeignKey(to=Tag, to_field='id', on_delete=CASCADE, verbose_name='帖子分类')
    hit = models.IntegerField(verbose_name='点赞次数', default=0)
    creatTime = models.DateTimeField(verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='帖子更新时间')

    class Meta:
        db_table = "PostInfo"
        ordering = ['-creatTime']
        verbose_name = '帖子信息表'


class PostSource(models.Model):
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE, verbose_name='帖子id')
    url = models.URLField(max_length=200, default=None, null=True, verbose_name='资源下载地址')
    imgName = models.CharField(max_length=100, default=None, null=True, verbose_name='图片名称')
    imgFile = models.ImageField(upload_to='post/img', default=None, null=True, verbose_name='图片存放地址')
    video = models.URLField(max_length=200, default=None, null=True, verbose_name='视频播放地址')

    class Meta:
        db_table = "postSource"
        verbose_name = '帖子资源信息表'


class Comment(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='评论id')
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE, verbose_name='评论的帖子')
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE, verbose_name='评论的用户id')
    text = models.TextField(max_length=200, verbose_name='评论内容')
    creatTime = models.DateTimeField()

    class Meta:
        db_table = "comment"
        ordering = ['-creatTime']
        verbose_name = '评论信息表'


class CommentRelationship(models.Model):
    comment = models.ForeignKey(to=Comment, to_field='id', on_delete=CASCADE, verbose_name='评论id')
    up_comment = models.CharField(max_length=20, default=None, null=True, verbose_name='上一条评论的id')

    class Meta:
        db_table = "CommentRelationship"
        verbose_name = '评论信息关系表'


class CommentSource(models.Model):
    comment = models.ForeignKey(to=Comment, to_field='id', on_delete=CASCADE)
    url = models.URLField(max_length=200, default=None, null=True, verbose_name='评论图片路径')
    imgName = models.CharField(max_length=100, verbose_name='图片名称')
    imgFile = models.ImageField(upload_to='comment/img', default=None, null=True, verbose_name='图片路径')

    class Meta:
        db_table = "commentSource"
        verbose_name = '评论资源信息表'


class Collection(models.Model):
    user = models.ForeignKey(to=User, to_field='id', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE)
    creatTime = models.DateTimeField()

    class Meta:
        db_table = "Collection"
        ordering = ['-creatTime']
        verbose_name = '用户收藏信息表'


class Source(models.Model):
    post = models.ForeignKey(to=Post, to_field='id', on_delete=CASCADE, verbose_name='帖子id')
    comment = models.ForeignKey(to=Comment, to_field='id', default=None, null=True, on_delete=CASCADE, verbose_name='评论id')
    filename = models.CharField(max_length=100, default=None, null=True, verbose_name='图片名称')
    url = models.URLField(max_length=200, verbose_name='评论图片路径')
    type = models.CharField(max_length=10, default=None, verbose_name='资源类型')
    creatTime = models.DateTimeField()

    class Meta:
        db_table = 'Source'
        ordering = ['-creatTime']
        verbose_name = '所有资源信息表'
