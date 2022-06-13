from .models import Assign, Exam, Question, QuizTaker, Answer, subject
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])

        valid_list = ['ankitssharma198@gmail', 's.ankitsharma198@gmail.com']

        if user.email in valid_list:

            user.is_staff = True
            user.save()
        else:
            user.save()

        return user


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['category', 'description', 'optiion1', 'optiion2', 'optiion3', 'optiion4']

    def to_representation(self, instance):
        ret = super(QuestionSerializer, self).to_representation(instance)

        ret['category'] = instance.category.Subject.subject
        return ret


class ExamSerializer(serializers.ModelSerializer):
    Question = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['teacher', 'Subject', 'Question']
        read_only_fields = ['teacher', 'Question']

    def create(self, validated_data):
        validated_data['teacher'] = self.context['request'].user
        val = Exam.objects.filter(teacher=validated_data.get('teacher')).filter(
            Subject=validated_data.get('Subject', None))
        print(val.first())
        if val.first() is None:
            validated_data['teacher'] = self.context['request'].user
            return super().create(validated_data)
        else:
            raise serializers.ValidationError(
                "subject with this teacher already")

    def to_representation(self, instance):
        ret = super(ExamSerializer, self).to_representation(instance)
        ret['Subject'] = instance.Subject.subject
        ret['teacher'] = instance.teacher.username
        return ret


class QuizzTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ('user', 'exam', 'correct_answers')

    def to_representation(self, instance):
        ret = super(QuizzTakerSerializer, self).to_representation(instance)
        ret['user'] = instance.user.username
        ret['exam'] = instance.exam.Subject.subject
        return ret


class AssignexamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = ['Student', 'exam']

    def to_representation(self, instance):
        ret = super(AssignexamSerializer, self).to_representation(instance)
        ret['Student'] = instance.Student.username
        ret['exam'] = instance.exam.Subject.subject

        return ret


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'Answer']

    def to_representation(self, instance):
        ret = super(AnswerSerializer, self).to_representation(instance)
        ret['question'] = instance.question.description

        return ret


class subserializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ['subject']
