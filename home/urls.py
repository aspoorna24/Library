from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home, name= "home"),
    path("Librarian",views.Librarian, name = 'Librarian'),
    path("Students", views.Students, name='Students'),
    path("main",views.main, name="main"),
    path("mains",views.mains, name="mains"),
    path("error",views.error, name="error"),
    path("book",views.book, name="book"),
    path("sreg",views.sreg, name="sreg"),
    path("sl", views.sl,name="sl"),
    path("insertbook",views.insertbook,name="insertbook"),
    path("bookava",views.bookava,name="bookava"),
    path("booklib",views.booklib,name="booklib"),
    path("issue",views.issue,name="issue"),
    path("issulist",views.issulist,name="issulist"),
    path("retur",views.retur,name="retur")

]
