from django.urls import re_path

from . import exceptions, views

app_name = 'api'

urlpatterns = [
    re_path(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'^snippets2/$', views.SnippetList.as_view(), name='snippet2-list'),
    re_path(r'^snippet/(?P<pk>\d+)/$', views.SnippetDetail.as_view(),
        name='snippet-detail'),

    re_path(r'^server_error/$', exceptions.server_error, name='server-error'),
    re_path(r'^not_found/$', exceptions.not_found, name='not-found'),
    re_path(r'^method_not_allowed/$', exceptions.method_not_allowed,
        name='not-allowed'),
    re_path(r'^not_authenticated/$', exceptions.not_authenticated,
        name='not-authenticated'),
]
