:orphan:

.. _third-party:

Python 2.4 で動かないサードパーティライブラリ
==================================================

これまで見てきたように Python 2.4 はより新しいバージョンと比べると
様々な違いがあります。特に Python 3 で行われた構文上の変更の多くが
Python 2.4 と Python 3 のサポートを両立させることを困難にします。
そのため、サードパーティのライブラリも徐々に Python 2.4 のサポートを
打ち切って Python 3 への対応を進めつつあるのが現状です。

ここでは、主に Web 開発で使われるサードパーティのライブラリについて、
最新のバージョンでは Python 2.4 で動かないものを列挙します。

サードパーティのライブラリは非常に数が多いため、このリストは網羅的で
ないことに注意してください。また、状況は今後も変化するので、
現在は Python 2.4 で動くライブラリであっても、バージョンアップの度に
変更履歴を確認するようにしてください。
(もっと良いのは buildbot や Jenkins でインストールの自動テストを
動かしておくことです)

webob
----------

`webob <http://webob.org/>`_ は WSGI アプリケーションでリクエストとレスポンス
をラップしたオブジェクトを提供するライブラリです。

webob 1.1 で Python 2.5 以下のサポートが打ち切られ、一部のコードで
``with`` 構文等が使われるようになったため Python 2.4 では動作しません。
Python 2.4 をサポートする最後のバージョンである 1.0.8 を使ってください。

easy_install を使う場合::

  $ easy_install webob==1.0.8

pip を使う場合::

  $ pip webob==1.0.8

(以下同様)

Beaker
----------

`Beaker <http://beaker.readthedocs.org/en/latest/>`_ は
WSGI アプリケーションにキャッシュとセッションの機能を提供するライブラリです。

Beaker 1.6 以降は一部のコードで ``with`` 構文が使われているため
Python 2.4 では動作しません。
最新版の代わりに 1.5.4 を使ってください。

PasteDeploy
--------------------

`PasteDeploy <http://pythonpaste.org/deploy/>`_ は
WSGI アプリケーションのデプロイに関係する様々な機能を含むライブラリです。

PasteDeploy 1.5.0 で Python 2.4 のサポートが打ち切られ、一部のコードで
条件演算子等が使われるようになったため Python 2.4 では動作しません。
Python 2.4 をサポートする最後のバージョンである 1.3.4 を使ってください。

IPy
----------

`IPy <http://pypi.python.org/pypi/IPy/>`_ は IP アドレスに関する演算を
行うライブラリです。

IPy 0.73 で Python 2.4 のサポートが打ち切られ、一部のコードで ``with``
構文等が使われるようになったため Python 2.4 では動作しません。
最新版の代わりに 0.72 を使ってください。

PyYAML
----------

`PyYAML <http://pyyaml.org/wiki/PyYAML>`_ は Python で YAML
(Yet Another Markup Language) を読み書きするためのライブラリです。

PyYAML 3.10 で Python 2.4 のサポートが打ち切られ、一部のコードで
``try-finally`` ブロック内部で ``yield`` が使われているため Python 2.4 では
動作しません。
最新版の代わりに 3.09 を使ってください。

rsa
----------

`rsa <http://stuvel.eu/files/python-rsa-doc/index.html>`_ は pure Python
による RSA の実装です。

rsa 3.0 では Python 2.6 以降にのみ存在する :mod:`abc` モジュールが
使われているため Python 2.4 では動作しません。
最新版の代わりに 1.3.3 を使ってください。

decorator
----------

`decorator <http://pypi.python.org/pypi/decorator/>`_ は :ref:`functools`
でも紹介したデコレータを書くためのライブラリです。

decorator 3.4.0 では条件演算子が使われているため Python 2.4 では動作しません。
最新版の代わりに 3.3.3 を使ってください。

simplejson
----------

`simplejson <http://pypi.python.org/pypi/simplejson/>`_ は :ref:`json`
でも紹介した JSON を Python で扱うためのライブラリです。

simplejson 2.1.0 で Python 2.4 はサポートされなくなり、
2.4.0 では条件演算子が使われているため Python 2.4 では動作しません。
最新版の代わりに 2.3.3 を使ってください。
