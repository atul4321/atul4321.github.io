from rest_framework import permissions
from .serializers import AnswerSerializer, AssignexamSerializer, QuestionSerializer, RegisterSerializer,\
    ExamSerializer, QuizzTakerSerializer, subserializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, SAFE_METHODS
from .models import Answer, Exam, Question, QuizTaker, subject, Assign


class Register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class Exam(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]


class Question(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]


class IsOwnerOfObject(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        return obj.user == request.user


class Taker(viewsets.ModelViewSet):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizzTakerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsOwnerOfObject, IsAdminUserOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class Answer(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]


class Assign(viewsets.ModelViewSet):
    queryset = Assign.objects.all()
    serializer_class = AssignexamSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]


class Subject(viewsets.ModelViewSet):
    queryset = subject.objects.all()
    serializer_class = subserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUserOrReadOnly]
