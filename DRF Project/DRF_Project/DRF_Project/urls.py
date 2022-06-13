from django.contrib import admin
from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('Register As a Teacher And Student', views.Register, basename='Registration')
router.register('Quiz-details',views.Exam,basename='Exam')
router.register('Questions',views.Question,basename='Question')
router.register('Quiz Score',views.Taker,basename='Taker')
router.register('Answer',views.Answer,basename='Answer')
router.register('Add Subject',views.Subject,basename='Subject')
router.register("Assign Exam To Student",views.Assign,basename="Assign")
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]
