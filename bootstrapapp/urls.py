from django.urls import path
from bootstrapapp import views

urlpatterns = [
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('service/',views.service,name='my_service'),
    path('gallery/',views.gallery,name='my_gallery'),
    path('contact/',views.contact,name='my_contact'),    
]