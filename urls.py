from django.conf.urls import url
from .views import TemplateAPIView

urlpatterns = [
	path('template/', TemplateAPIView.as_view()),
	]
