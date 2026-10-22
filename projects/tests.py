from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Project


class ProjectTests(TestCase):

    def setUp(self):
        self.p = Project.objects.create(
            title="Demo Project", slug="demo-project",
            summary="A demo", description="Long story",
            technologies="Django, React", category="web",
            github_url="https://example.com/repo")

    def test_home_lists_project(self):
        response = self.client.get(reverse("project_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Demo Project")

    def test_card_links_to_detail(self):
        response = self.client.get(reverse("project_list"))
        self.assertContains(response, reverse("project_detail", args=("demo-project",)))

    def test_detail_page(self):
        response = self.client.get(reverse("project_detail", args=("demo-project",)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Long story")
        self.assertContains(response, "https://example.com/repo")

    def test_detail_404(self):
        response = self.client.get(reverse("project_detail", args=("nope",)))
        self.assertEqual(response.status_code, 404)

    def test_tech_filter(self):
        Project.objects.create(title="Other", slug="other",
                               summary="s", description="d",
                               technologies="Flask", category="other")
        response = self.client.get(reverse("project_list") + "?tech=Flask")
        self.assertContains(response, "Other")
        self.assertNotContains(response, "Demo Project")

    def test_search(self):
        response = self.client.get(reverse("project_list") + "?q=long")
        self.assertContains(response, "Demo Project")

    def test_slug_is_unique(self):
        with self.assertRaises(IntegrityError):
            Project.objects.create(title="Dup", slug="demo-project",
                                   summary="s", description="d")

    def test_tech_list_parses_commas(self):
        self.assertEqual(self.p.tech_list(), ["Django", "React"])
