from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers

from polls_app.models import *


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
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    question_set = QuestionSerializer(many=True)
    is_my = serializers.SerializerMethodField('get_is_my')
    is_voted = serializers.SerializerMethodField('get_is_voted')

    def get_is_my(self, poll):
        request = self.context.get('request', None)
        if request:
            return request.user.id == poll.creator.pk
        return False

    def get_is_voted(self, poll):
        request = self.context.get('request', None)
        if request:
            for question in poll.question_set.all():
                for answer in question.answer_set.all():
                    try:
                        if UserToAnswer.objects.filter(user=request.user.id, answer=answer).__len__() != 0:
                            return True
                    except UserToAnswer.DoesNotExist:
                        pass
        return False

    class Meta:
        model = Poll
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)
    creator_id = serializers.IntegerField(
        default=serializers.CurrentUserDefault()
    )
    creator = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Poll
        fields = "__all__"


class PollCreateSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Poll
        fields = "__all__"

    def create(self, validated_data):

        poll = Poll(title=validated_data['title'], description=validated_data['description'],
                    voting_time=validated_data['voting_time'], theme=validated_data['theme'],
                    creator=validated_data['creator'])
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


class UserToAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        received_user = validated_data['user']
        if isinstance(received_user, AnonymousUser):
            received_user = None
        user_to_answer = UserToAnswer(user=received_user, answer=validated_data['answer'])
        user_to_answer.save()
        return user_to_answer

    class Meta:
        model = UserToAnswer
        fields = "__all__"
