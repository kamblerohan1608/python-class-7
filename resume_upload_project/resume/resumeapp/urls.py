from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('all_candidates/',views.all_candidates.as_view(),name='all_candidates'),
    path('candidate_info/<int:pk>',views.candidate_info.as_view(),name='candidate_info'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('about/',views.about.as_view(),name='about'),
    path('delete/<int:pk>',views.delete.as_view(),name='delete'),
    path('update/<int:pk>',views.update.as_view(),name='update'),

]