from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from todoapi.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^register/', 'todoapi.views.register'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

