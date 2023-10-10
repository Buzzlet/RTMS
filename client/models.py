from django.db import models

# Create your models here.
class User(models.Model):
    user_id     = models.CharField("Unique User ID", max_length=20)
    user_name   = models.CharField("User Name", max_length=40)
    user_lvl    = models.IntegerField("User Level", default=0)
    user_status = models.CharField("User Status", max_length=10)
    last_login  = models.DateTimeField("Last Login")
    bad_logins  = models.IntegerField("Bad Logins", default=0)
    
    def __str__(self):
        return self.user_id
    
class Ticket(models.Model):
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    tkt_num       = models.CharField("Ticket Number", max_length=10)
    title         = models.CharField("Ticket Title", max_length=50)
    description   = models.CharField("Ticket Desciption", max_length=255)
    status        = models.CharField("Ticket Status", max_length=10)
    priority      = models.IntegerField("Ticket Priority", default=0)
    precedence    = models.IntegerField("Ticket Prcedence", default=0)
    requestor     = models.CharField("Ticket Requestor", max_length=50)
    plant         = models.CharField("Ticket Plant", max_length=10)
    assigned_to   = models.CharField("Ticket Assigned To", max_length=20)
    create_date   = models.DateTimeField("Ticket Create Date")
    goal_date     = models.DateTimeField("Ticket Goal Date")
    complete_date = models.DateTimeField("Ticket Complete Date")
    branch        = models.CharField("Ticket Branch", max_length=40)
    
    def __str__(self):
        return self.user_id + " - " + self.tkt_num + " - " + self.title
    
class Task(models.Model):
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
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
    create_date   = models.DateTimeField("Task Create Date")
    goal_date     = models.DateTimeField("Task Goal Date")
    complete_date = models.DateTimeField("Task Complete Date")
    branch        = models.CharField("Task Branch", max_length=40)
    
    def __str__(self):
        return self.user_id + " - " + self.tkt_num + " - " + self.task_num + " - " + self.title
    
class Note(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    tkt_num  = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    task_num = models.ForeignKey(Task, on_delete=models.CASCADE)
    note     = models.CharField("Note", max_length=255)
    
    def __str__(self):
        return self.user_id + " - " + self.tkt_num + " - " + self.task_num + " - " + self.note
    