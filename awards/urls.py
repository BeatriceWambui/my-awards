from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^subscribe/',views.mysubscribe,name = 'subscribe'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/$',views.uploadProfile,name='uploadProfile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/merch/$',views.ProjectList.as_view()),
    url(r'^upload/$',views.UploadProject,name='UploadProject'),
    url(r'^api_-token-auth/',obtain_auth_token),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
