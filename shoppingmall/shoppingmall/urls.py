from django.conf.urls import patterns, include, url

from django.contrib import admin
from views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoppingmall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',hello),
    url(r'^mall/',Malls),
    url(r'^malldetail/',ShowDetail)
)
