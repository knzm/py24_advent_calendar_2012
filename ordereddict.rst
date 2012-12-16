:orphan:

.. _ordereddict:

:class:`OrderedDict` がない
==============================

:class:`dict` の特徴は、保存したデータ量によらず検索が ``O(1)`` で行えることです。
それと引き換えに、 :class:`dict` は保存したキーの順番を維持しません。

.. code-block:: pycon

  >>> d = {}
  >>> d["zero"] = 0
  >>> d["one"] = 1
  >>> d["two"] = 2
  {'zero': 0, 'two': 2, 'one': 1}

すべてのキーをある決まった順番で処理したい時は、 :func:`sorted` 関数を使って
キーをソートします。

あまり意味のある例ではありませんが、キーをアルファベット順でソートする
コードはこのようになります。

.. code-block:: pycon

  >>> for key in sorted(d.keys()):
  ...     print key, "=>", d[key]
  ... 
  one => 1
  two => 2
  zero => 0

キーの順番を維持してほしいケースというのは意外と多くありません。
とはいえ、たまにあると便利なことは確かです。例えばプログラムで選択肢を扱う場合、
表示するテキストとプログラム内部で使う値の両方を持つ必要があり、
表示する順番も指定した通りになってくれないと困ります。こういうときは 
Python 2.7 から追加された :class:`OrderedDict` を使います。

.. code-block:: pycon

  $ python2.7
  >>> from collections import OrderedDict
  >>> d = OrderedDict()
  >>> d["zero"] = 0
  >>> d["one"] = 1
  >>> d["two"] = 2
  >>> for key in d.keys():
  ...     print key, "=>", d[key]
  ... 
  zero => 0
  one => 1
  two => 2

`PyPI <http://pypi.python.org/pypi>`_ から :mod:`ordereddict`
モジュールをインストールすれば Python 2.4 でも :class:`OrderedDict` を使えます。

.. note::

   Python の歴史上、これまでにいくつも同じような名前と機能を持つライブラリが
   作られてきました。
   `PEP 372 <http://www.python.org/dev/peps/pep-0372/>`_ に
   その一覧があります。
