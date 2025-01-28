from django.contrib.auth.models import User
from django.test import TestCase

from .models import Lesson


class LessonModelTest(TestCase):
    def setUp(self):
        # Set up initial data for the tests
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            slug="test-lesson",
            author=self.user,
            content="This is a test lesson content.",
        )

    def test_lesson_creation(self):
        # Test the creation of a lesson
        self.assertEqual(self.lesson.title, "Test Lesson")
        self.assertEqual(self.lesson.slug, "test-lesson")
        self.assertEqual(self.lesson.author, self.user)
        self.assertEqual(self.lesson.content, "This is a test lesson content.")

    def test_lesson_str(self):
        # Test the string representation of a lesson
        self.assertEqual(str(self.lesson), "Test Lesson")

    def test_lesson_slug(self):
        # Test the slug field of a lesson
        pass

    def test_lesson_author(self):
        # Test the author field of a lesson
        pass

    def test_lesson_content(self):
        # Test the content field of a lesson
        pass

    def test_lesson_created_on(self):
        # Test the created_on field of a lesson
        pass

    def test_lesson_updated_on(self):
        # Test the updated_on field of a lesson
        pass


class QuestionModelTest(TestCase):
    def setUp(self):
        # Set up initial data for the tests
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            slug="test-lesson",
            author=self.user,
            content="This is a test lesson content.",
        )

    def test_question_creation(self):
        # Test the creation of a question
        pass

    def test_question_str(self):
        # Test the string representation of a question
        pass

    def test_question_body(self):
        # Test the body field of a question
        pass

    def test_question_preset_answer(self):
        # Test the preset_answer field of a question
        pass

    def test_question_questiontype(self):
        # Test the questiontype field of a question
        pass

    def test_question_lesson(self):
        # Test the lesson field of a question
        pass

    def test_question_due_date(self):
        # Test the due_date field of a question
        pass

    def test_question_created_on(self):
        # Test the created_on field of a question
        pass

    def test_question_updated_on(self):
        # Test the updated_on field of a question
        pass
