from django.views.generic import ListView
from .models import Job

class JobListView(ListView):
    model = Job
    template_name = 'job_board/index.html'
    context_object_name = 'job_list'
