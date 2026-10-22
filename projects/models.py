from django.db import models


class Project(models.Model):
    """One portfolio card. The detail page is generated from these fields."""

    CATEGORY_CHOICES = [
        ('web', 'Web App'),
        ('api', 'API / Backend'),
        ('fullstack', 'Full Stack'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,
        help_text="URL name: my-project -> /project/my-project/")
    summary = models.CharField(max_length=160,
        help_text="One line shown ON the card")
    description = models.TextField(
        help_text="Full story shown on the detail page")
    image = models.ImageField(upload_to='projects/', blank=True, null=True,
        help_text="Screenshot (1200x630 looks best)")
    technologies = models.CharField(max_length=200,
        help_text="Comma separated: Django, DRF, React, ...")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
        default='web')
    project_url = models.URLField(blank=True,
        help_text="Live demo link (leave empty if none)")
    github_url = models.URLField(blank=True)
    completed = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=True,
        help_text="Featured projects appear first")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-completed', '-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        # "Django, DRF, React" -> ["Django", "DRF", "React"]
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
