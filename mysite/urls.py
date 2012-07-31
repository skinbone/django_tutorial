from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^polls/', include('polls.urls')),
    # the regular expression doesn't have a $ (end-of-string match character)
    # but has the trailing slash. Whenever Django encounters include(),
    # it chops off whatever part of the URL matched up to that point
    # and sends the remaining string to the included URLconf for further processing.

    url(r'^admin/', include(admin.site.urls)),
)
