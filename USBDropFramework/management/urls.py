from django.conf.urls import include, url, patterns

from management.views import TargetListView, TestListView

urlpatterns = patterns('',
    url(r'^$', TargetListView.as_view(), name='target_list'),
    url(r'^target/(?P<pk>\d+)/$', TestListView.as_view(), name='test_list'),
    # url(r'^target/(?P<pk>\d+)/test/(?P<pk>\d+)/$', TestView.as_view(), name='test_view'),
)