from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import UserProfileListCreate, UserProfileRetrieveUpdateDestroy
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Создаем экземпляр DefaultRouter
router = DefaultRouter()
# Регистрируем наши ViewSet'ы с роутером
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)

# URL-маршруты для наших API представлений
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('myproject.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profiles/', UserProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroy.as_view(), name='profile-retrieve-update-destroy'),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
