from rest_framework.decorators import api_view
from rest_framework.response import Response
from questionnaire.models import UserQuestionnaire
from questionnaire.models import Questionnaire
from django.contrib.auth.models import User
# Create your views here.


@api_view(['GET'])
def get_all_questions(request):
    if request.method == 'GET':
        try:
            questionnaire = Questionnaire.objects.all()
            my_questions = []
            for data in questionnaire:
                my_questions.append(
                    {
                        'textInputName': data.questions,
                        'textInputTime': data.time
                    }
                )
            return Response({'response': my_questions})
        except:
            return Response({'response': 'invalid_response'})


@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        try:
            users = UserQuestionnaire.objects.select_related('user').all()
            user_data = []
            for user in users:
                user_data.append(
                    {
                        'username': user.username,
                        'email': user.email,
                        'location': user.location,
                        'question': user.questionnaire,
                        'recording': user.recording
                    }
                )
            return Response({'response': user_data})
        except:
            return Response({'response': 'invalid response'})

@api_view(['POST'])
def add_or_delete_question(request):
    if request.method == 'POST':
        print(request.data)
        text = request.data['action']
        
        if text == 'added':
            question = request.data['question']
            Questionnaire.objects.create(questions=question)
            return Response({'response': 'question_added'})
        elif text == 'delete':
            question = request.data['question']
            if Questionnaire.filter(questions=question).exist():
                record = Questionnaire.objects.get(questions=question)
                record.delete()
                return Response({'response': 'question_deleted'})

@api_view(['POST'])
def update_time(request):
    if request.method == 'POST':
        username = request.user.username
        timer = request.data['time']
        question = request.data['question']

        timer = Questionnaire.objects.filter(questions=question)
        timer.time = timer
        timer.save()
        return Response({'response': 'question_added'})


