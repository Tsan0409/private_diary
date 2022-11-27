from django.urls import path

from.import views


# app_name 他のアプリとの衝突を避けるため
app_name = 'diary'
# path(:https//<ホスト名>, IndexView.as_views(=クラスを関数形式に), name(=ルーティング処理の識別))
# 第一引数とパターンがマッチングすれば、第二引数の処理を行う。第3引数のnameはルーティングの名前でURLを逆引きする時に使う
#アプリケーション側のパターンマッチングは管理サーバーのパターンにプラスで加えるもの。
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]
