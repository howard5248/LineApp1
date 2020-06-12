# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account = models.CharField(db_column='Account', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purview = models.IntegerField(db_column='Purview', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='Logindate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account'


class LineAccount(models.Model):
    account = models.CharField(db_column='Account', primary_key=False, max_length=50)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    LineID = models.CharField(db_column='LineID', primary_key=True, max_length=50)
    LineName = models.CharField(db_column='LineName', primary_key=False, max_length=50)
    LinePic = models.CharField(db_column='LinePic', primary_key=False, max_length=200)

    class Meta:
        managed = True
        db_table = 'LineAccount'