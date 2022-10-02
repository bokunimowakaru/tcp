#!/usr/bin/env python3
# coding: utf-8

# TCPを送信する
# Copyright (c) 2021-2022 Wataru KUNINO

# TCPで文字列'Ping'を送信します。
# ./ex1_tx.py

import socket                                               # ソケットの組み込み

port = 8080                                                 # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.connect(('127.0.0.1', port))                           # TCP接続
tcp = 'Ping\n'                                              # 送信文字列
sock.send(tcp.encode())                                     # メッセージ送信
sock.close()                                                # ソケットの切断

''' ----------------------------------------------------------------------------
TCPサーバ側：
pi@raspberry:~/tcp/learning $ ./ex2_rx.py
Listening TCP port 8080 ...
127.0.0.1 59850
Ping

--------------------------------------------------------------------------------
TCPクラアント側(★本プログラム)：
pi@raspberry:~/tcp/learning $ ./ex1_tx.py
---------------------------------------------------------------------------- '''
