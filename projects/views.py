from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):
    """Home page: every project as a card, with tech filter + search."""
    projects = Project.objects.all()

    # filter chips: /?tech=Django  or  /?q=react
    tech = request.GET.get("tech", "").strip()
    if tech:
        projects = projects.filter(technologies__icontains=tech)

    q = request.GET.get("q", "").strip()
    if q:
        projects = projects.filter(
            Q(title__icontains=q) | Q(summary__icontains=q)
            | Q(technologies__icontains=q) | Q(description__icontains=q)
        )

    # unique tech names for the filter bar, sorted
    all_tech = sorted({
        t.strip()
        for p in Project.objects.values_list("technologies", flat=True)
        for t in p.split(",") if t.strip()
    })

    return render(request, "projects/project_list.html", {
        "projects": projects,
        "all_tech": all_tech,
        "active_tech": tech,
        "q": q,
    })


def project_detail(request, slug):
    """The page a card click leads to."""
    project = get_object_or_404(Project, slug=slug)
    others = Project.objects.exclude(pk=project.pk)[:3]
    return render(request, "projects/project_detail.html", {
        "project": project,
        "others": others,
    })
