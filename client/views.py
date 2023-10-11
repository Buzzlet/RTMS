from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import User, Ticket, Task, Note

# Create your views here.
def index(request):
    usr = User.objects.get(userid="jristvedt")
    user_tickets = usr.ticket_set.order_by("precedence")
    # template = loader.get_template("client/index.html")
    context = {
        "usr": usr,
        "user_tickets": user_tickets,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, "client/index.html", context)
    
def ticket(request, tkt_num):

    return HttpResponse("You're looking at ticket %s." % tkt_num)
    
def task(request, tkt_num, task_num):
    return HttpResponse("You're looking at ticket %(tkt)s task %(task)d." % 
                        {'tkt': tkt_num, 'task': task_num})

def note(request, tkt_num, task_num, note_id):
    return HttpResponse("You're looking at note %d." % note_id)