from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('create_event', views.createEvent, name= 'create_event'),
    path('update_event/<int:pk>', views.updateEvent, name = 'update_event' ),
    path('delete_event/<int:pk>', views.updateEvent, name = 'delete_event' ),
]  

