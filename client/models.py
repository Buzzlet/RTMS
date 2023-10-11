from django.db import models

# Create your models here.
class User(models.Model):
    userid      = models.CharField("Unique User ID", max_length=20, unique=True)
    user_name   = models.CharField("User Name", max_length=40)
    user_lvl    = models.IntegerField("User Level", default=0)
    user_status = models.CharField("User Status", max_length=10)
    last_login  = models.DateTimeField("Last Login", blank=True, null=True)
    bad_logins  = models.IntegerField("Bad Logins", default=0)
    
    def __str__(self):
        return self.userid
    
class Ticket(models.Model):
    userid        = models.ForeignKey(User, on_delete=models.CASCADE)
    tkt_num       = models.CharField("Ticket Number", max_length=10)
    title         = models.CharField("Ticket Title", max_length=50)
    description   = models.CharField("Ticket Desciption", max_length=255)
    status        = models.CharField("Ticket Status", max_length=10)
    priority      = models.IntegerField("Ticket Priority", default=0)
    precedence    = models.IntegerField("Ticket Prcedence", default=0)
    requestor     = models.CharField("Ticket Requestor", max_length=50)
    plant         = models.CharField("Ticket Plant", max_length=10)
    assigned_to   = models.CharField("Ticket Assigned To", max_length=20)
    create_date   = models.DateTimeField("Ticket Create Date", blank=True, null=True)
    goal_date     = models.DateTimeField("Ticket Goal Date", blank=True, null=True)
    complete_date = models.DateTimeField("Ticket Complete Date", blank=True, null=True)
    branch        = models.CharField("Ticket Branch", max_length=40)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userid', 'tkt_num'], name="%(app_label)s_%(class)s_unique")
        ]
    
    def __str__(self):
        return self.tkt_num
    
class Task(models.Model):
    userid        = models.ForeignKey(User, on_delete=models.CASCADE)
    tkt_num       = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    task_num      = models.IntegerField("Task Number", default=0)
    title         = models.CharField("Task Title", max_length=50)
    description   = models.CharField("Task Desciption", max_length=255)
    status        = models.CharField("Task Status", max_length=10)
    priority      = models.IntegerField("Task Priority", default=0)
    precedence    = models.IntegerField("Task Prcedence", default=0)
    requestor     = models.CharField("Task Requestor", max_length=50)
    plant         = models.CharField("Task Plant", max_length=10)
    assigned_to   = models.CharField("Task Assigned To", max_length=20)
    create_date   = models.DateTimeField("Task Create Date", blank=True, null=True)
    goal_date     = models.DateTimeField("Task Goal Date", blank=True, null=True)
    complete_date = models.DateTimeField("Task Complete Date", blank=True, null=True)
    branch        = models.CharField("Task Branch", max_length=40)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userid', 'tkt_num', 'task_num'], name="%(app_label)s_%(class)s_unique")
        ]
    
    def __str__(self):
        return self.task_num
    
class Note(models.Model):
    userid   = models.ForeignKey(User, on_delete=models.CASCADE)
    tkt_num  = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    task_num = models.ForeignKey(Task, on_delete=models.CASCADE)
    note     = models.CharField("Note", max_length=255)
    
    def __str__(self):
        return self.note
    