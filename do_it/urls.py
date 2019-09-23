from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from do_it.views import index_page, home_page


urlpatterns = [
    path('', index_page),
    path('home', home_page, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', include(('signup.urls', 'signup'), namespace="signup")),
    path('staff/', include(('staff.urls', 'staff'), namespace='staff')),
    path('doer/', include(('doer.urls', 'doer'), namespace='doer')),
    path('core/', include(('core.urls', 'core'), namespace='core')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
