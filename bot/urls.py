from django.conf.urls import url
from . import views
#from callback.views import CallbackView

urlpatterns = [
  url(r'^$', views.post_test),
]