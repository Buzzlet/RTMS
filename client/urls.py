from django.urls import path, include

from . import views

app_name = "client"
urlpatterns = [
    # ex: /client/
    path("", views.index, name="index"),
    # ex: /client/accounts/
    path("accounts/", include("django.contrib.auth.urls")), 
    # ex: /client/453623
    path("<str:tkt_num>/", views.ticket, name="ticket"),
    # ex: /client/453623/1
    path("<str:tkt_num>/<int:task_num>/", views.task, name="task"),
    # ex: /client/453623/1/254
    path("<str:tkt_num>/<int:task_num>/<int:note_id>/", views.note, name="note"),
    # ex: /client/453623/swap/482134
    path("<str:tkt_num1>/swap/<str:tkt_num2>/", views.swap, name="swap"),
]