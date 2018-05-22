from django.conf.urls import include, url
from django.urls import path
import articles.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()
import hello.views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)