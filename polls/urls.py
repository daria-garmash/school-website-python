from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main'),
    path('equipment/', views.show_equipment, name='equipment'),
    path('best/', views.show_best_graduates, name='best'),
    path('graduation/', views.show_graduation, name='graduation'),
    path('test/', views.show_test, name='test'),
    path('traditions/', views.show_traditions, name='traditions'),
    path('<dark>', views.changemode),
    path('form/', views.getform, name='form'),
    path('table/', views.apps_info, name='table'),

]
