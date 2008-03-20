from django.conf.urls.defaults import *
from django.contrib.auth import views
from django.views.generic import simple

urlpatterns = patterns('',
    # Example:
    # (r'^implist/', include('implist.foo.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^login/$', views.login),
    (r'^login/$', views.logout),
    (r'^register/$', views.login),
    
)

urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'G:/tapicks/news/templates/site_media'}),
        (r'^dummy/', simple.direct_to_template, {'template':'news/dummy.html'})
    )

urlpatterns += patterns('news.subscriptions',
    url(r'^subscribe/(?P<topic_name>[^\.^/]+)/$', 'subscribe', name='subscribe'),
    url(r'^unsubscribe/(?P<topic_name>[^\.^/]+)/$', 'unsubscribe', name='unsubscribe'),
    
)

urlpatterns += patterns('news.topics',
    url(r'^$', 'main', name='main'),                        
    (r'^create_topic/', 'create'),
    url(r'^(?P<topic_name>[^\.^/]+)/$', 'topic_main', name='topic'),
    
)

urlpatterns += patterns('news.tags',
    url(r'^(?P<topic_name>[^\.^/]+)/tag/(?P<tag_text>[^\.^/]+)/$', 'topic_tag', name='topic_tag'),
    url(r'^tag/(?P<tag_text>[^\.^/]+)/$', 'sitewide_tag', name='sitewide_tag'),
)

urlpatterns += patterns('news.links',
    url(r'^(?P<topic_name>[^\.^/]+)/submit/$', 'link_submit', name='link_submit'),
    url(r'^up/(?P<link_id>\d+)/$', 'upvote_link', name='upvote_link'),
    url(r'^down/(?P<link_id>\d+)/$', 'downvote_link', name='downvote_link'),
    url(r'^(?P<topic_name>[^\.^/]+)/(?P<link_id>\d+)/$', 'link_details', name='link_detail'),
)