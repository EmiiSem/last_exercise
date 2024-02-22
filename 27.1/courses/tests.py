from django.test import TestCase
from .models import Lesson
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Course, CourseSubscription

class LessonCRUDTests(TestCase):
    def test_lesson_creation(self):
        lesson = Lesson.objects.create(title="New Lesson", content="Lesson Content")
        self.assertEqual(lesson.title, "New Lesson")

    def test_lesson_reading(self):
        lesson = Lesson.objects.create(title="New Lesson", content="Lesson Content")
        retrieved_lesson = Lesson.objects.get(title="New Lesson")
        self.assertEqual(retrieved_lesson.content, "Lesson Content")

    def test_lesson_update(self):
        lesson = Lesson.objects.create(title="New Lesson", content="Lesson Content")
        lesson.title = "Updated Lesson Title"
        lesson.save()
        self.assertEqual(lesson.title, "Updated Lesson Title")

    def test_lesson_deletion(self):
        lesson = Lesson.objects.create(title="To Be Deleted", content="Delete Me")
        lesson.delete()
        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(title="To Be Deleted")

class CourseSubscriptionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(title='Test Course')
  
    def test_subscription_set_and_delete(self):
        subscription = CourseSubscription.objects.create(user=self.user, course=self.course)
        self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())
      
        subscription.delete()
        self.assertFalse(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())
