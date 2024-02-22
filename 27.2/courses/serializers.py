from rest_framework import serializers
from .models import Course, Lesson, User
from .models import UserProfile
from rest_framework import serializers
from .models import Course
from .models import CourseSubscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'city', 'avatar']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_subscribed(self, obj):
        # Проверка подписки текущего пользователя на курс
        user = self.context['request'].user
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj).exists()
        return False
