from django.conf.urls import url
from django.views.generic import ListView,DetailView
from . import views
from .models import Post

app_name = 'myapp'

urlpatterns = [
    url(r'^contact/',views.contact,name='contact'),#retrieve data through dictonary

    url(r'^blog/', ListView.as_view(queryset=Post.objects.all(),template_name="myapp/blog.html")),  #retrieve from db

   # url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="myapp/post.html")),

   # url(r'^(?P<pk>\d+)$', views.DetailsView.as_view(),name='post'),

    url('form/',views.cred,name='form'),

    url(r'^$',views.IndexView.as_view(), name='index'),  # normal

    url('sum1/', views.sum, name='sum1'),

    url('sum2/', views.sum, name='sum2'),

    url('makeentry/', views.makeentry, name='makeentry'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),

    url('today/', views.daysweek, name='today'),

    url('mod/', views.startview.as_view(), name='index1'),  # normal

]