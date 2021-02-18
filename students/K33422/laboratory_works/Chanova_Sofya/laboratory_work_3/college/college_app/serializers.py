from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField(source="get_role_display")
    student_group = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'role', 'first_name', 'last_name', 'email', 'student_group', 'teacher_qualification']


class EditUserProfileSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField(source="get_role_display")
    student_group = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name', 'email', 'student_group', 'teacher_qualification']


class UserSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField(source="get_role_display")

    class Meta:
        model = User
        fields = ['username', 'role', 'first_name', 'last_name', 'email']


class StudentSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField(source="get_role_display")
    student_group = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'role', 'first_name', 'last_name', 'email', 'student_group']


class TeacherSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField(source="get_role_display")

    class Meta:
        model = User
        fields = ['username', 'role', 'first_name', 'last_name', 'email', 'teacher_qualification']


class StudentGroupSerializer(serializers.ModelSerializer):

    group_number = serializers.CharField(max_length=10,
                                         validators=[UniqueValidator(queryset=StudentGroup.objects.all())])

    class Meta:
        model = StudentGroup
        fields = '__all__'


class StudentGroupCreateSerializer(serializers.Serializer):

    group_number = serializers.CharField(max_length=10,
                                         validators=[UniqueValidator(queryset=StudentGroup.objects.all())])
    course_number = serializers.IntegerField()
    department = serializers.CharField(max_length=30)

    def create(self, validated_data):
        group = StudentGroup(**validated_data)
        group.save()
        return StudentGroup(**validated_data)


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleEntry
        fields = '__all__'

    weekday = serializers.StringRelatedField(source="get_weekday_display")
    time = serializers.StringRelatedField(source="get_time_display")

    room_number = serializers.CharField(read_only=True)
    group_number = serializers.CharField(read_only=True)
    teacher = serializers.CharField(read_only=True)
    subject = serializers.CharField(read_only=True)


class ScheduleCreateSerializer(serializers.Serializer):

    weekday = serializers.ChoiceField(choices=ScheduleEntry.weekdays)
    time = serializers.ChoiceField(choices=ScheduleEntry.lessons)

    room_number = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    group_number = serializers.PrimaryKeyRelatedField(queryset=StudentGroup.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='t'))
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    def create(self, validated_data):
        schedule = ScheduleEntry(**validated_data)
        schedule.save()
        return ScheduleEntry(**validated_data)


class RoomPageSerializer(serializers.ModelSerializer):

    room_number = serializers.IntegerField(validators=[UniqueValidator(queryset=Room.objects.all())])

    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    subject_theme = serializers.StringRelatedField(source='get_subject_theme_display')
    room_number = serializers.IntegerField(validators=[UniqueValidator(queryset=Room.objects.all())])


    class Meta:
        model = Room
        fields = '__all__'


class RoomCreateSerializer(serializers.Serializer):

    room_number = serializers.IntegerField(validators=[UniqueValidator(queryset=Room.objects.all())])
    seats_quantity = serializers.IntegerField()
    subject_theme = serializers.ChoiceField(choices=Room.themes)

    def create(self, validated_data):
        room = Room(**validated_data)
        room.save()
        return Room(**validated_data)


class SubjectSerializer(serializers.ModelSerializer):

    control_type = serializers.StringRelatedField(source='get_control_type_display')

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectCreateSerializer(serializers.Serializer):

    subject_name = serializers.CharField(max_length=50)
    control_type = serializers.ChoiceField(choices=Subject.types)
    academic_hours = serializers.IntegerField(default=36)
    description = serializers.CharField(max_length=300, allow_blank=True)

    def create(self, validated_data):
        subject = Subject(**validated_data)
        subject.save()
        return Subject(**validated_data)


class SemesterGradeSerializer(serializers.ModelSerializer):

    subject = serializers.CharField(source='teaching.subject')
    student = serializers.CharField(read_only=True)
    graded_by = serializers.CharField(source='teaching.teacher')
    grade = serializers.ChoiceField(choices=SemesterGrade.grades)

    class Meta:
        model = SemesterGrade
        fields = ['student', 'subject', 'grade', 'graded_by']


class SemesterGradeCreateSerializer(serializers.Serializer):

    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='s'))
    teaching = serializers.PrimaryKeyRelatedField(queryset=Teaching.objects.all())
    grade = serializers.ChoiceField(choices=SemesterGrade.grades)

    def create(self, validated_data):
        grade = SemesterGrade(**validated_data)
        grade.save()
        return SemesterGrade(**validated_data)


class TeachingSerializer(serializers.ModelSerializer):

    teacher = serializers.CharField(read_only=True)
    subject = serializers.CharField(read_only=True)

    class Meta:
        model = Teaching
        fields = '__all__'


class TeachingCreateSerializer(serializers.Serializer):

    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='t'))
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    def create(self, validated_data):
        teaching = Teaching(**validated_data)
        teaching.save()
        return Teaching(**validated_data)
