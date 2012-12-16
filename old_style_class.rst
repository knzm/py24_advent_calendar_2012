:orphan:

.. _old-style-class:

:class:`Exception` が :class:`object` のサブクラスではない
============================================================

Python には New-style class と Old-style class という 2 種類のクラスが
存在します。その違いを一言でいうと :class:`object` を継承しているかどうかです。

Old-style class と New-style class の例:

::

  class Old:
      """Old-style class"""
      pass

  class New(object):
      """New-style class"""
      pass

2 種類のクラスが存在するのは主に歴史的な理由によるものなので、
新規に書くコードでは Old-style class を使う理由はありません。
また Python 3 では Old-style class が廃止されて
どちらの書き方でも New-style class になります。

例外クラス :class:`Exception` は Python 2.4 以前は Old-style class でした。
そのため、以下のようなコードは Python 2.5 以上では動きますが、
Python 2.4 ではエラーになります。

::

  class APIError(Exception):
      def __init__(self, code):
          super(APIError, self).__init__(code)

Python 2.5 の実行結果:

::

  >>> APIError(1)
  APIError(1,)

Python 2.4 の実行結果:

::

  >>> APIError(1)
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "<stdin>", line 3, in __init__
  TypeError: super() argument 1 must be type, not classobj

このバグは、特に本番環境が Python 2.4 で普段の開発環境では 2.5 や 2.6 を
使っている場合に起こりがちです。こうしたバージョン毎の微妙な違いによる
罠を避けるため、開発環境のバージョンを常に本番環境と揃えている開発者もいます。
しかし、普段使う開発環境で Python 2.4 を常用するのも辛いものがあるので、
自動テスト環境を用意して複数のバージョンでテストを実行するのが良いと思います。

`Jenkins <http://jenkins-ci.org/>`_ や `buildbot <http://trac.buildbot.net/>`_
を使えば簡単に自動テスト環境を構築することができます。
複数バージョンでのテストは `tox <http://pypi.python.org/pypi/tox>`_ が便利です。
また最近では `Travis-CI <https://travis-ci.org/>`_ や
`Shining Panda <https://www.shiningpanda-ci.com/>`_
といったサービスもあります。

「継続的インテグレーション (Continuous Integration; CI)」などのキーワードで
検索すれば入門的な記事も含めて様々な情報が見つかるので、ぜひ試してみてください。
