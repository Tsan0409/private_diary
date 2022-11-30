from django import forms

import os

from django import forms
from django.core.mail import EmailMessage

from .models import Diary


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields['<フィールド名>'].widget.attrs['属性名']  CSS属性の操作
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'ここに名前を入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'

    def send_email(self):

        # self.cleaned_data['<フィールド名>'>]
        # バリデーションを通った入力値の取得(バリデーション=必須項目の入力、入力書式, 最大値等がただし以下の確認）
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = f'お問合せ {title}'
        message = f'送信者名: {name}\nメールアドレス: {email}\nメッセージ:\n{message}'
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
