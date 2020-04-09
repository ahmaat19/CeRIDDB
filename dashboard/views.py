from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Project
from .forms import ProjectModelForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def HomeView(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/accounts/login/')


@login_required
def ProjectView(request): 
    if request.user.groups.all()[0].name in ['Admin', 'Executive Director', 'Project Manager']:
        project_list = Project.objects.order_by('-id')
    else:
        project_list = Project.objects.filter(created_by=request.user.id).order_by('-id')

    paginator = Paginator(project_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = project_list.count()
    if queryset:
        queryset = Project.objects.filter(Q(title__icontains=queryset))
        total = queryset.count()
    context = {
        'queryset': queryset,
        'total': total,
        'projects': projects
    }
    return render(request, 'dashboard/projects.html', context)


@login_required
def ProjectCreateView(request):   
    form = ProjectModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Project added successfully.')
        return redirect('/projects/')

    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Create Project',
    }
    return render(request, 'dashboard/project_create.html', context)


@login_required
def ProjectUpdateView(request, pk):
    if request.user.groups.all()[0].name in ['Admin', 'Executive Director', 'Project Manager']:
        project = get_object_or_404(Project, pk=pk)
    else:
         project = get_object_or_404(Project, pk=pk, created_by=request.user.id)
    form = ProjectModelForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Project was updated successfully.')
        return redirect('/projects/')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Project',
    }
    return render(request, 'dashboard/project_create.html', context)


@login_required
def ProjectDetailView(request, pk):
    if request.user.groups.all()[0].name in ['Admin', 'Executive Director', 'Project Manager']:
        project = get_object_or_404(Project, pk=pk)
    else:
        project = get_object_or_404(Project, pk=pk, created_by=request.user.id)
    context = {
        'title': 'Project Details',
        'project': project
    }
    return render(request, 'dashboard/project_detail.html', context)