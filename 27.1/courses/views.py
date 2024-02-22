from rest_framework import viewsets, generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsModeratorOrReadOnly
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CourseSubscription
from .serializers import CourseSubscriptionSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import stripe
from .tasks import send_course_update_email

class YourAPIView(ListCreateAPIView):
    permission_classes = [IsModeratorOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CourseSubscriptionCreate(generics.CreateAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer

    def perform_create(self, serializer):
        # Установка подписки для текущего пользователя и курса
        serializer.save(user=self.request.user)

class CourseSubscriptionDelete(generics.DestroyAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer

    def get_object(self):
        # Получение объекта подписки для текущего пользователя и курса
        return CourseSubscription.objects.get(user=self.request.user, course_id=self.kwargs['course_id'])

class LessonsList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = PageNumberPagination  # Использование стандартной пагинации

class CoursesList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = PageNumberPagination  # Использование стандартной пагинации

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20  # Размер страницы по умолчанию
    page_size_query_param = 'page_size'  # Параметр запроса для изменения размера страницы
    max_page_size = 100  # Максимальный размер страницы

class CoursesList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPageNumberPagination  # Использование настраиваемой пагинации

stripe.api_key = "my_key"

def create_payment_intent(request, amount, currency='usd'):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )
    #код для обработки созданного платежа
    return intent

def retrieve_payment_intent(request, payment_intent_id):
    intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    #код для обработки полученной информации о платеже
    return intent

new_material = "Новый урок"
course_id = 123  # ID курса, для которого добавлен новый материал

send_course_update_email.delay(course_id, new_material)