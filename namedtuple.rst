.. _namedtuple:

:class:`namedtuple` がない
==============================

:class:`namedtuple` というのは名前付きのタプルです。
なくてもなんとかなるものの、あると地味に便利な機能の一つです。

Python にはタプルというデータ構造があり、任意個の値の組を一つの値として
扱うことができます。

例えば、時刻を数値の組で表すとこんな感じになると思います。

::

  >>> dt = (2012, 12, 25, 23, 59, 59)

(これは2012年12月25日23時59分59秒を表しているつもりです)

この値から年や分などの個別の値を取り出そうとすると、タプルの中の位置を指定して
以下のように書くことになります (注: 位置は 0 から数えます)。

::

  >>> year = dt[0]
  >>> minute = dt[4]

これの問題点は、何番目に何の値が入っているかをいちいち数えないと
このコードが正しいかどうかわからないということです。
以下のコードは間違っていますが、すぐに気がつきますか？

::

  >>> minute = dt[5]

:class:`namedtuple` を使うと、位置に加えて属性名でも参照することができます。

::

  >>> from collections import namedtuple
  >>> DateTime = namedtuple('DateTime', 'year month day hour minute second')
  >>> dt = DateTime(2012, 12, 25, 23, 59, 59)
  >>> dt[0]
  2012
  >>> dt.year
  2012
  >>> dt.minute
  59

名前で参照する方が圧倒的に分かりやすいですね。

Python 2.6 から :class:`namedtuple` が追加され、標準ライブラリのいくつかのモジュールで、これまでタプルを返していた関数が :class:`namedtuple` を返すように変更されました。
代表例は URL を要素に分解して一部を取り出す際に使う :func:`urlsplit` 関数です。

::

  >>> from urlparse import urlsplit
  >>> o = urlsplit('http://www.example.com:80/index.cgi?cmd=read#top')
  >>> o
  SplitResult(scheme='http', netloc='www.example.com:80', path='/index.cgi', query='cmd=read', fragment='top')
  >>> o.path
  '/index.cgi'

タプルとしてもアクセスできるので、従来のコードとも互換性があります。

::

  >>> scheme, netloc, path, query, fragment = o

Python 2.4 ではこの書き方しかできません。

----

以下、主にプログラマ向けの注釈です。

実際には上記の例にあるような DateTime 型を定義する必要はなく、
:class:`datetime` クラスの :meth:`~datetime.timetuple` メソッドが返す
:class:`time.struct_time` クラスを使うことができます。

::

  >>> import datetime
  >>> dt = datetime.datetime(2012, 12, 25, 23, 59, 59).timetuple()
  >>> dt
  time.struct_time(tm_year=2012, tm_mon=12, tm_mday=25, tm_hour=23, tm_min=59, tm_sec=59, tm_wday=1, tm_yday=360, tm_isdst=-1)

余談ですが、この :class:`time.struct_time` 型は :class:`namedtuple` かと思ったら違いました。

::

  >>> isinstance(dt, tuple)
  False
  >>> dt.__class__.mro()
  [<type 'time.struct_time'>, <type 'object'>]

比較のため、 :class:`urlsplit` の戻り値の型を調べてみると、
:class:`tuple` のサブクラスのインスタンスであることが分かります。

::

  >>> from urlparse import urlsplit
  >>> o = urlsplit('http://www.example.com:80/index.cgi?cmd=read#top')
  >>> isinstance(o, tuple)
  True
  >>> o.__class__.mro()
  [<class 'urlparse.SplitResult'>, <class 'urlparse.SplitResult'>, <type 'tuple'>, <class 'urlparse.ResultMixin'>, <type 'object'>]

:mod:`time` が C 拡張モジュールなので、そのせいかとも思うのですが、
詳細は分かりません。
