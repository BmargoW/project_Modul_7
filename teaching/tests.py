from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient
from teaching.models import Lesson, Course, Subscription
from users.models import CustomUser


class CourseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(email="drug@mail.ru", username="Drug")
        self.course = Course.objects.create(title="IT", description="test", owner=self.user)
        self.lesson = Lesson.objects.create(name="Electronic", description="Edison", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("teaching:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "IT"
        )

    def test_course_create(self):

        url = reverse("teaching:course-list")
        data = {
            "title": "SQL",
            "description": "good",
            "lessons": [
                {
                    "name": "Basics",
                    "description": "First steps",
                    "video_url":"https://www.youtube.com/watch?v=8sv-6AN0_cg",
                    "course":self.course.pk,

                }
            ],
        }
        response = self.client.post(url, data, format="json")
        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_data = response.json()

        self.assertEqual(created_data.get("title"), "SQL")
        self.assertIn("lessons", created_data)
        self.assertEqual(len(created_data["lessons"]), 1)

    def test_course_update(self):
        url = reverse("teaching:course-detail", args=(self.course.pk,))
        data = {
            "title": "SQL-bd",
            "description": "good",
            "lessons": [
                {
                    "name": "Basics",
                    "description": "First steps",
                    "video_url": "https://www.youtube.com/watch?v=8sv-6AN0_cg",
                    "course": self.course.pk,

                }
            ],
        }
        response = self.client.patch(url)
        print("Status:", response.status_code)
        print("Response JSON:", response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "SQL-bd"
        )

    def test_course_delete(self):
        url = reverse("teaching:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)
        print("Status:", response.status_code)


        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
    def test_course_list(self):

        url = reverse("teaching:course-list")

        response = self.client.get(url)

        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(email="drug@mail.ru", username="Drug")
        self.course = Course.objects.create(title="IT", description="test", owner=self.user)
        self.lesson = Lesson.objects.create(name="Electronic", description="Edison", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("teaching:l-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Electronic"
        )

    def test_lesson_create(self):

        url = reverse("teaching:l-create")
        data =  {
                    "name": "Basics",
                    "description": "First steps",
                    "video_url":"https://www.youtube.com/watch?v=8sv-6AN0_cg",
                    "course":self.course.pk,

                }

        response = self.client.post(url, data, format="json")
        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_data = response.json()

        self.assertEqual(created_data.get("name"), "Basics")

    def test_lesson_update(self):
        url = reverse("teaching:l-update", args=(self.lesson.pk,))

        data = {
            "name": "Second",
            "description": "First steps",
            "video_url": "https://www.youtube.com/watch?v=8sv-6AN0_cg",
            "course": self.course.pk,

        }
        response = self.client.patch(url)
        print("Status:", response.status_code)
        print("Response JSON:", response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Second"
        )

    def test_lesson_delete(self):
        url = reverse("teaching:l-delete", args=(self.lesson.pk,))

        response = self.client.delete(url)
        print("Status:", response.status_code)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_lesson_list(self):

        url = reverse("teaching:l-list")

        response = self.client.get(url)

        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionViewTest(APITestCase):

    def setUp(self):

        self.user = CustomUser.objects.create(email="drug@mail.ru", username="Drug")
        self.course = Course.objects.create(title="IT", description="test", owner=self.user)

        self.client.force_authenticate(user=self.user)

        self.url = reverse('teaching:course-subscribe', kwargs={'course_id': self.course.pk})

    def test_subscribe_success(self):
        """Успешное создание подписки"""
        response = self.client.post(self.url)
        data = response.json()
        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['detail'], 'Подписка оформлена')
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())