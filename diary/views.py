import logging

from django.urls import reverse_lazy

from django.shortcuts import render

from django.views import generic

from.forms import InquiryForm

from django.contrib import messages

logger = logging.getLogger(__name__)

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    # フォームのバリデーションが問題なければ動くメソッド
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info(f'Inquiry sent by {form.cleaned_data["name"]}')
        return super().form_valid(form)
