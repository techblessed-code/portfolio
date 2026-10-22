from datetime import date

from django.core.management.base import BaseCommand

from projects.models import Project


class Command(BaseCommand):
    help = "Creates the 4 starter portfolio projects"

    def handle(self, *args, **options):
        data = [
            dict(
                title="Wiki Encyclopedia",
                slug="wiki-encyclopedia",
                summary="A Wikipedia clone where every entry is a Markdown file.",
                description=(
                    "Encyclopedia with full CRUD over Markdown entries stored on "
                    "disk (no database): list all entries, render Markdown to HTML, "
                    "search with exact-match redirect and partial matching, create "
                    "entries with case-insensitive duplicate protection, edit with a "
                    "pre-filled form, and a random-page button. Ships with a test "
                    "suite and clean 404/error pages."),
                technologies="Django, Markdown, Bootstrap, SQLite",
                category="web",
                github_url="https://github.com/techblessed-code/wiki-encyclopedia",
                completed=date(2026, 9, 1),
            ),
            dict(
                title="Airline Booking",
                slug="airline-booking",
                summary="Flight booking: airports, flights, passengers, full CRUD.",
                description=(
                    "CS50-style airline extended into a full CRUD app: airports, "
                    "flights and many-to-many passenger booking. Includes server-side "
                    "validation (numeric duration, no same-airport flights), "
                    "404-instead-of-500 handling, CSRF-protected POST mutations, "
                    "Bootstrap UI with booking form, and a 22-test suite covering "
                    "models, views and every edge case."),
                technologies="Django, SQLite, Bootstrap, unittest",
                category="web",
                github_url="https://github.com/techblessed-code/airline",
                completed=date(2026, 10, 22),
            ),
            dict(
                title="Dunis LMS",
                slug="dunis-lms",
                summary="5-app learning platform: courses, auth, CBV and a REST API.",
                description=(
                    "A learning management system split into five Django apps: "
                    "courses (function-based CRUD with image uploads), users "
                    "(register/login/dashboard), landing pages, a class-based-view "
                    "variant of the course CRUD behind LoginRequiredMixin, and a "
                    "Django REST Framework API. Session auth, namespaced URLs, "
                    "security-hardened settings and 12 passing tests."),
                technologies="Django, DRF, Pillow, Bootstrap, SQLite",
                category="fullstack",
                github_url="https://github.com/techblessed-code/dunislms",
                completed=date(2026, 10, 12),
            ),
            dict(
                title="ShopKid E-commerce",
                slug="shopkid-ecommerce",
                summary="React SPA on a JWT-secured Django REST API: cart & orders.",
                description=(
                    "Full e-commerce stack: Django REST Framework backend with "
                    "products, categories, per-user carts, checkout that freezes "
                    "prices into order snapshots and restores stock on cancel; "
                    "SimpleJWT auth with automatic token refresh; staff order "
                    "dashboard; product image uploads. Frontend is a React 18 SPA "
                    "with axios interceptors, auth/cart contexts, protected routes "
                    "and 14 pages."),
                technologies="DRF, SimpleJWT, React, axios, Bootstrap",
                category="fullstack",
                github_url="https://github.com/techblessed-code/shopkid-e-commerce",
                completed=date(2026, 10, 6),
            ),
        ]
        for item in data:
            obj, created = Project.objects.get_or_create(slug=item["slug"], defaults=item)
            self.stdout.write(("  + " if created else "  = ") + obj.title)
        self.stdout.write(self.style.SUCCESS("Done."))
