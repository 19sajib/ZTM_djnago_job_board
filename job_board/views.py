from django.shortcuts import render, get_object_or_404

from .models import JobPosting

def index(request):
    # jobs = JobPosting.objects.all()
    acitve_posting = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': acitve_posting
    }
    return render(request, 'job_board/index.html' , context)

def job_detail(request, pk):
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        'posting': job_posting
    }
    
    return render(request, 'job_board/detail.html', context)