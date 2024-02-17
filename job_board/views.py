from django.shortcuts import render, HttpResponse

from .models import JobPosting

def index(request):
    # jobs = JobPosting.objects.all()
    acitve_posting = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': acitve_posting
    }
    return render(request, 'job_board/index.html' , context)