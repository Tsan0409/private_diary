import logging

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from .forms import InquiryForm, DiaryCreateForm
from .models import Diary

logger = logging.getLogger(__name__)


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


# 　　　　　　　　　　　↓ログイン必須クラス    ↓データをリストアップして表示するクラス
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-create_at')
        return diaries


class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'


class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        # diary {user: false, diary: aaa, photo: / exam.jpg}
        diary = form.save(commit=False)
        # user = user_id　をデータベースから代入
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記の作成に失敗しました')
        return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記の更新に失敗しました')


class DiaryDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '日記を削除しました')
        return super().delete(request, *args, **kwargs)
