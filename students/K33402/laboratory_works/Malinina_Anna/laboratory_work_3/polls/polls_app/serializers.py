from rest_framework import serializers

from polls_app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",
                  "username",
                  "name",
                  "email",
                  "date_of_birth"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"


class PollDetailsSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        exclude = ['creator']


class PollCreateSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['creator']

        poll = Poll(title=validated_data['title'], description=validated_data['description'],
                    voting_time=validated_data['voting_time'], theme=validated_data['theme'], creator=user)
        poll.save()
        for question in validated_data['question_set']:
            question_instance = Question.objects.create(description=question['description'], poll=poll)
            question_instance.save()
            for answer in question['answer_set']:
                answer_instance = Answer.objects.create(description=answer['description'], question=question_instance)
                answer_instance.save()
        return poll

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.voting_time = validated_data['voting_time']
        instance.theme = validated_data['theme']
        instance.save()

        questions = list(instance.question_set.all())

        for input_question in validated_data['question_set']:
            question = questions.pop(0)
            question.description = input_question['description']
            question.poll = instance
            question.save()
            answers = list(question.answer_set.all())

            for input_answer in input_question['answer_set']:
                answer = answers.pop(0)
                answer.description = input_answer['description']
                answer.question = question
                answer.save()

        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['answers']

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    answers_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Answer.objects.all(),
                                                     source='answers')

    class Meta:
        model = User
        exclude = ['answers']


class UserDetailsSerializer(serializers.ModelSerializer):
    poll_set = PollSerializer(many=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
