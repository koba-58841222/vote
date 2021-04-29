from django import forms
from . models import Question
from . models import User
 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('contents', 'choice_a','choice_b','choice_c','choice_d')
        labels={
           'contents':'アンケート内容',
           'choice_a':'選択肢A',
           'choice_b':'選択肢B',
           'choice_c':'選択肢C',
           'choice_d':'選択肢D',
           }
