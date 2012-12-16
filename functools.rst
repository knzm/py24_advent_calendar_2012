:orphan:

.. _functools:

:mod:`functools` がない
==============================

Python の便利な機能の一つにデコレータ構文があります。
デコレータとは関数(Python 2.6 からはクラスも)を修飾するもので、
既存の関数(やクラス)に新しい機能や意味を付け加えます。

以下の例で ``@trace`` の部分がデコレータ構文です。
また :func:`trace` 関数自体のことをデコレータと呼びます。

::

  def trace(f):
      def wrapper(x):
          print "enter"
          try:
              return f(x)
          finally:
              print "leave"
      return wrapper

  @trace
  def f(x):
      print x

実行結果

::

  >>> f("hello")
  enter
  hello
  leave

アスペクト指向のようなことが簡単に実現できました。

実は上記の例には少しだけ問題があって、デコレータを適用する前の関数の情報が
失われています。

::

  >>> f.__name__
  'wrapper'

これは :func:`trace` 関数がその中で定義した :func:`wrapper` をそのまま
返しているためです。
ここで元の関数 :func:`f` の情報を :func:`wrapper` にセットしてやれば
良いのですが、ちゃんとやろうとすると結構大変です。

Python 2.5 からは :mod:`functools` モジュールの :func:`wraps` 関数を使って
正しいデコレータを簡単に書くことができます。

::

  from functools import wraps

  def trace(f):
      @wraps(f)
      def wrapper(x):
          print "enter"
          try:
              return f(x)
          finally:
              print "leave"
      return wrapper

デコレータ定義の中でデコレータ (``@wraps(f)``) が使われているのが
なんだか面白いですね。

Python 2.4 では、サードパーティの `decorator モジュール
<http://pypi.python.org/pypi/decorator/>`_ を使って同様のことが実現できます。

::

  from decorator import decorator

  @decorator
  def trace(f, x):
      print "enter"
      try:
          return f(x)
      finally:
          print "leave"

.. note::

   残念ながら :mod:`decorator` の最新版である 3.4.0 は Python 2.5 以降の構文を
   使用しているため Python 2.4 には対応していないようです。
   代わりに以前のバージョンの 3.3.3 をインストールしてください。
