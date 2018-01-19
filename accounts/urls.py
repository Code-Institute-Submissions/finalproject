from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, logout, login, subscribe, cancel_subscription, subscriptions_webhook, contactus, faq

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', subscriptions_webhook, name='subscriptions_webhook'),
    url(r'^contact/$', contactus, name='contact'),
    url(r'^faq/$', faq, name='faq'),
    
    
]