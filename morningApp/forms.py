from django import forms
from . models import Question
 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('id', 'contents', 'choice_a','choice_b','choice_c','choice_d')
        labels={
            'id':'ID',
           'contents':'アンケート内容',
           'choice_a':'選択肢A',
           'choice_b':'選択肢B',
           'choice_c':'選択肢C',
           'choice_d':'選択肢D',
           }