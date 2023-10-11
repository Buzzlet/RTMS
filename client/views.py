from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import User, Ticket, Task, Note

# Create your views here.
def index(request):
    usr = get_object_or_404(User, userid="jristvedt")
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
    
def swap(request, tkt_num1, tkt_num2):
    usr = get_object_or_404(User, userid="jristvedt")
    tkt = usr.ticket_set.get(tkt_num=tkt_num1)
    tkt2 = usr.ticket_set.get(tkt_num=tkt_num2)
    tmp = tkt2.precedence
    tkt2.precedence = tkt1.precedence
    tkt1.precedence = tmp
    tkt1.save()
    tkt2.save()
    response_date = {'success':1}
    return HttpResponse(json.dumps(response_date), content_type="application/json")