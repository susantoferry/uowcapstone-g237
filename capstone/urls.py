from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category", views.category, name="category"),
    path("add_category", views.addCategory, name="add_category"),
    path("edit_category/<id>", views.editCategory, name="edit_category"),
    path("delete_category/<id>", views.deleteCategory, name="delete_category"),
    path("create_ticket", views.createTicket, name="create_ticket"),
    path("save_ticket", views.saveTicket, name="save_ticket"),
    path("tickets", views.searchTicket, name="search_ticket"),
    path("ticket_list/<ticket_name>", views.ticketList, name="ticket_list"),
    path("ticket_detail/<ticket_id>/<ticket_name>", views.ticketDetail, name="ticket_detail"),
    path("notification", views.notification, name="notification"),
    path("read_ticket/<ticket_id>", views.readTicket, name="read_ticket"),
    path("async_notification/<userId>", views.asyncNotification),
    path("get_role/<roleId>", views.getRole),
    path("get_suitable_users", views.getSuitableUsers),
    path("profile", views.profile, name="profile"),
    path("user", views.users, name="user"),
    path("save_questionnaire", views.saveQuestionnaire, name="save_questionnaire"),
    path("questionnaire/<username>", views.questionnaire, name="questionnaire"),
    path("mbti_result/<username>", views.mbtiResult, name="mbti_result"),    
    
    path("login", views.loginView, name="login"),
    path("register", views.registerView, name="register"),
    path("logout", views.logoutView, name="logout"),
]