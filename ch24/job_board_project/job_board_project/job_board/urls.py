from django.urls import path
from .views import JobListView


urlpatterns = [
    # Job URLs
    path('', JobListView.as_view(), name='job_list'),
]
