from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User

from .models import Guide


class GuideTestCase(TestCase):
    username = 'testusername'
    password = 'testpassword'
    guide_title = 'My Test Guide'
    guide_slug = slugify(guide_title)

    def setUp(self):
        User.objects.create_user(username=self.username, password=self.password)
        user = User.objects.first()
        Guide.objects.create(
            author=user,
            title=self.guide_title,
            description='My Test Guide Description',
            content='My Test Guide Content',
            category='PvM',
            approved=True
        )

    def test_guide_slug(self):
        """Tests if the slug field of Guide is correctly being saved"""
        guide = Guide.objects.get(title=self.guide_title)
        self.assertEqual(guide.slug, self.guide_slug)

    def test_unique_slug(self):
        """Tests if the slugs being created are actually unique, even with Guides of the same title existing"""
        user = User.objects.first()
        first_guide = Guide.objects.first()
        second_guide = Guide.objects.create(
            author=user,
            title=self.guide_title,
            description='',
            content='',
            category='PvM',
            approved=True
        )
        self.assertNotEqual(first_guide.slug, second_guide.slug)
        # The slug of a guide will be equal to it's sluggified title, a dash and then the count of guides with
        # that same name minus 1
        guides_count = Guide.objects.filter(title=self.guide_title).count()
        self.assertEqual(second_guide.slug, f'{self.guide_slug}-{guides_count - 1}')

    def test_approval_methods(self):
        """Tests if Guide.approve() and Guide.unapprove() methods are correctly working"""
        guide = Guide.objects.first()
        guide.unapprove()
        self.assertFalse(guide.approved)
        guide.approve()
        self.assertTrue(guide.approved)
