from django.urls import path

from.import views


# app_name 他のアプリとの衝突を避けるため
app_name = 'diary'
# path(:https//<ホスト名>, IndexView.as_views(=クラスを関数形式に), name(=ルーティング処理の識別))
# 第一引数とパターンがマッチングすれば、第二引数のビュークラスを呼び出す処理を行う。第3引数のnameはルーティングの名前でURLを逆引きする時に使う
#アプリケーション側のパターンマッチングは管理サーバーのパターンにプラスで加えるもの。
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary-create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),
]
