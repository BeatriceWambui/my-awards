from django.test import TestCase
from .models import Project
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='wamboh', password='wer2345uyq')
        self.user.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
    def test_save_user(self):
        self.user.save()
    def test_delete_user(self):
        self.user.delete()
        
class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='wamboh')
        self.project = Project.objects.create(id=1, title='test project', image='test.png', profile_image=self.user, link='prhfsjl.co.ke')
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)
    def test_get_project(self):
        self.project.save()
        project = Project.all_project()
        self.assertTrue(len(project) > 0)
    def test_search_project(self):
        self.project.save()
        project = Project.search_project('test')
        self.assertTrue(len(project) > 0)
    def test_delete_project(self):
        self.project.delete_project()
        project = Project.search_project('test')
        self.assertTrue(len(project) < 1)
