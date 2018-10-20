from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    url(r'^$', views.FileListView.as_view(), name='file_list'),
    url(r'^server/file/(?P<pk>\d+)$', views.FileDetailView.as_view(), name='file_detail'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^upload/', views.FileCreate.as_view(), name='upload_file'),
    # url(r'^print/(?P<pk>\d+)/$',views.show, name='show'),
    url(r'^mark/(?P<pk>\d+)/$',views.markPrinted, name='mark'),
    url(r'^new/',views.forgot, name='new'),
    url(r'^profile/',views.profile, name='profile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
