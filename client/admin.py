from django.contrib import admin
from .models import User, Ticket, Task, Note

# Register your models here.
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Task)
admin.site.register(Note)

