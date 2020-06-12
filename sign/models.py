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


class Answer(models.Model):
    answerid = models.CharField(db_column='AnswerId', primary_key=True, max_length=50)  # Field name made lowercase.
    questionid = models.CharField(db_column='QuestionId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answerdstr = models.CharField(db_column='AnswerDstr', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    answeracountid = models.CharField(db_column='AnswerAcountId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answerdate = models.DateTimeField(db_column='AnswerDate', blank=True, null=True)  # Field name made lowercase.
    doc = models.CharField(db_column='Doc', max_length=3000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Answer'


class Authority(models.Model):
    loginid = models.CharField(db_column='LoginId', primary_key=True, max_length=50)  # Field name made lowercase.
    menuno = models.CharField(db_column='MenuNo', max_length=50)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mark = models.CharField(db_column='Mark', max_length=300, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=2)  # Field renamed because it was a Python reserved word.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authority'
        unique_together = (('loginid', 'menuno', 'class_field'),)


class Calendardata(models.Model):
    calendardate = models.DateField(db_column='CalendarDate', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalendarData'


class Department(models.Model):
    departmentid = models.CharField(db_column='DepartmentId', primary_key=True, max_length=8)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Department'


class Dialyworkrecord(models.Model):
    dialyworkrecordid = models.CharField(db_column='DialyWorkRecordId', primary_key=True, max_length=50)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    workdate = models.DateField(db_column='WorkDate', blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='ProjectId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workitemid = models.CharField(db_column='WorkItemId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    isovertime = models.CharField(db_column='IsOverTime', max_length=1, blank=True, null=True)  # Field name made lowercase.
    workhours = models.DecimalField(db_column='WorkHours', max_digits=12, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    workcontent = models.TextField(db_column='WorkContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DialyWorkRecord'


class Employee(models.Model):
    empid = models.CharField(db_column='EmpId', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=300, blank=True, null=True)  # Field name made lowercase.
    directdepartment = models.CharField(db_column='DirectDepartment', max_length=8, blank=True, null=True)  # Field name made lowercase.
    directsupervisor = models.CharField(db_column='DirectSupervisor', max_length=8, blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=8, blank=True, null=True)  # Field name made lowercase.
    postalcode1 = models.CharField(db_column='PostalCode1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=300, blank=True, null=True)  # Field name made lowercase.
    postalcode2 = models.CharField(db_column='PostalCode2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=300, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.
    onboarddate = models.DateField(db_column='OnBoardDate', blank=True, null=True)  # Field name made lowercase.
    quitdate = models.DateField(db_column='QuitDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class Leavedata(models.Model):
    leaveno = models.CharField(db_column='LeaveNo', primary_key=True, max_length=50)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=4, blank=True, null=True)
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    hours = models.DecimalField(db_column='Hours', max_digits=12, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    notificationobject = models.CharField(db_column='NotificationObject', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    signempid = models.CharField(db_column='SignEmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeaveData'


class Leavetype(models.Model):
    leavetypeid = models.CharField(db_column='LeaveTypeId', primary_key=True, max_length=8)  # Field name made lowercase.
    leavename = models.CharField(db_column='LeaveName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeaveType'


class Member(models.Model):
    projectid = models.CharField(db_column='ProjectId', primary_key=True, max_length=50)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=8)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member'
        unique_together = (('projectid', 'account'),)


class Menu(models.Model):
    menuno = models.CharField(db_column='MenuNo', primary_key=True, max_length=50)  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    menuaddress = models.CharField(db_column='MenuAddress', max_length=300, blank=True, null=True)  # Field name made lowercase.
    parent = models.CharField(max_length=50, blank=True, null=True)
    layer = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=8000, blank=True, null=True)
    mark = models.CharField(db_column='Mark', max_length=300, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNo', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Onbusinessdata(models.Model):
    onbusinessno = models.CharField(db_column='OnBusinessNo', primary_key=True, max_length=50)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    maincontent = models.CharField(db_column='MainContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    hours = models.DecimalField(db_column='Hours', max_digits=12, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    notificationobject = models.CharField(db_column='NotificationObject', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    signempid = models.CharField(db_column='SignEmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnBusinessData'


class Overtimedata(models.Model):
    overtimeno = models.CharField(db_column='OvertimeNo', primary_key=True, max_length=50)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    maincontent = models.CharField(db_column='MainContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    hours = models.DecimalField(db_column='Hours', max_digits=12, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    notificationobject = models.CharField(db_column='NotificationObject', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    signempid = models.CharField(db_column='SignEmpId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OvertimeData'


class Project(models.Model):
    projectid = models.CharField(db_column='ProjectId', primary_key=True, max_length=50)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='Startdate', blank=True, null=True)  # Field name made lowercase.
    scheduledenddate = models.DateTimeField(db_column='ScheduledEnddate', blank=True, null=True)  # Field name made lowercase.
    realenddate = models.DateTimeField(db_column='RealEnddate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'


class Projectfunction(models.Model):
    projectid = models.CharField(db_column='ProjectId', primary_key=True, max_length=50)  # Field name made lowercase.
    functionid = models.CharField(db_column='FunctionId', max_length=50)  # Field name made lowercase.
    functionname = models.CharField(db_column='FunctionName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=8, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='Createdate', blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='Modifydate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectFunction'
        unique_together = (('projectid', 'functionid'),)


class Question(models.Model):
    questionid = models.CharField(db_column='QuestionId', primary_key=True, max_length=50)  # Field name made lowercase.
    questionname = models.CharField(db_column='QuestionName', max_length=300, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='ProjectId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FunctionId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    questiondstr = models.CharField(db_column='QuestionDstr', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    doc = models.CharField(db_column='Doc', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    sendid = models.CharField(db_column='SendId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='SendDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Question'


class Rockchip(models.Model):
    seqno = models.AutoField(db_column='SeqNo', primary_key=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=12, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=10, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=8, blank=True, null=True)  # Field name made lowercase.
    android_ver = models.CharField(db_column='Android_Ver', max_length=8, blank=True, null=True)  # Field name made lowercase.
    android_codename = models.CharField(db_column='Android_codename', max_length=6, blank=True, null=True)  # Field name made lowercase.
    version_s = models.CharField(db_column='Version_s', max_length=14, blank=True, null=True)  # Field name made lowercase.
    version_e = models.CharField(db_column='Version_e', max_length=14, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=12, blank=True, null=True)  # Field name made lowercase.
    variant = models.CharField(db_column='Variant', max_length=5, blank=True, null=True)  # Field name made lowercase.
    field_key = models.CharField(db_column='_Key', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'Rockchip'


class Workitem(models.Model):
    workitemid = models.CharField(db_column='WorkItemId', primary_key=True, max_length=8)  # Field name made lowercase.
    workitemname = models.CharField(db_column='WorkItemName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkItem'

