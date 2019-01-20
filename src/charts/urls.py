from django.contrib import admin
from django.conf.urls import url

from .views import HomeView, ChartData


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-chartdata'),
    url(r'^admin/', admin.site.urls),
]
