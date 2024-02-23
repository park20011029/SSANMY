from django.db import models
# After This Column, Its pasted from modelpy.txt

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Category(models.Model):
    category_id = models.BigIntegerField(db_column='CATEGORY_ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'category'


class Comment(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=255)  # Field name made lowercase.
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    post = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_ID')  # Field name made lowercase.
    com_content = models.CharField(db_column='COM_CONTENT', max_length=255)  # Field name made lowercase.
    com_created = models.DateTimeField(db_column='COM_CREATED')  # Field name made lowercase.
    com_updated = models.DateTimeField(db_column='COM_UPDATED')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'comment'


class Company(models.Model):
    comp_id = models.BigIntegerField(db_column='COMP_ID', primary_key=True)  # Field name made lowercase.
    comp_name = models.CharField(db_column='COMP_NAME', max_length=255)  # Field name made lowercase.
    comp_model = models.CharField(db_column='COMP_MODEL', max_length=255)  # Field name made lowercase.
    comp_url = models.TextField(db_column='COMP_URL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'company'


class Image(models.Model):
    image_id = models.BigIntegerField(db_column='IMAGE_ID', primary_key=True)  # Field name made lowercase.
    post = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_ID')  # Field name made lowercase.
    image_url = models.TextField(db_column='IMAGE_URL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'image'


class Post(models.Model):
    post_id = models.BigIntegerField(db_column='POST_ID', primary_key=True)  # Field name made lowercase.
    category_id = models.BigIntegerField(db_column='CATEGORY_ID')  # Field name made lowercase.
    post_title = models.CharField(db_column='POST_TITLE', max_length=300)  # Field name made lowercase.
    post_content = models.TextField(db_column='POST_CONTENT')  # Field name made lowercase.
    post_created = models.DateTimeField(db_column='POST_CREATED')  # Field name made lowercase.
    post_clicked = models.IntegerField(db_column='POST_CLICKED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'post'

class testPost(models.Model):
    test_title = models.CharField(db_column='POST_TITLE', max_length=400)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'testPost'

class Postcategory(models.Model):
    mapping_id = models.BigIntegerField(db_column='MAPPING_ID', primary_key=True)  # Field name made lowercase.
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='POST_ID')  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='CATEGORY_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'postcategory'


class Site(models.Model):
    site_id = models.CharField(db_column='SITE_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='POST_ID')  # Field name made lowercase.
    comp = models.ForeignKey(Company, models.DO_NOTHING, db_column='COMP_ID', blank=True, null=True)  # Field name made lowercase.
    site_url = models.TextField(db_column='SITE_URL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'site'


class User(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=255)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=255)  # Field name made lowercase.
    user_nickname = models.CharField(db_column='USER_NICKNAME', max_length=255)  # Field name made lowercase.
    user_created = models.DateTimeField(db_column='USER_CREATED')  # Field name made lowercase.
    user_description = models.CharField(db_column='USER_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'