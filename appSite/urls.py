from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index/index.html'),name='index'),
    path('1', TemplateView.as_view(template_name='index/test.html'), name='index2')
]