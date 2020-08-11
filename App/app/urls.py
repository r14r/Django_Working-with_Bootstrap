"""
"""
from django.urls import path

from . import views
from django.conf.urls import handler404, handler500

app_name = 'app'
urlpatterns = [
    path('',                    views.ExamplesView.as_view(), name='index'),
    path('examples/',           views.ExamplesView.as_view(), name='examples'),
    path('example/<str:name>/', views.show_example,           name='example'),
    path('help/',               views.HelpView.as_view(),     name='help')
]

#handler404 = views.error404
#handler500 = views.error500
