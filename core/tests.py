from django.test import TestCase
from django.urls import reverse

from .models import Message


class CoreTests(TestCase):

    def test_root_renders_project_list(self):
        # "/" is served by projects.project_list (core.urls has no "" route -
        # a home redirect there would loop, since project_list also lives at "/")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Projects")

    def test_about_and_contact_render(self):
        self.assertEqual(self.client.get(reverse("about")).status_code, 200)
        self.assertEqual(self.client.get(reverse("contact")).status_code, 200)

    def test_contact_post_saves_message(self):
        response = self.client.post(reverse("contact"), {
            "name": "A Client", "email": "c@example.com",
            "subject": "Job", "body": "We need an API."})
        self.assertRedirects(response, reverse("contact"))
        self.assertTrue(Message.objects.filter(name="A Client").exists())

    def test_contact_invalid_form_shows_errors(self):
        response = self.client.post(reverse("contact"), {"name": "", "email": "bad"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "errorlist")
        self.assertEqual(Message.objects.count(), 0)
