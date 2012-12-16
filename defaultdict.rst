:orphan:

.. _defaultdict:

:class:`defaultdict` がない
==============================

Python の基本的なデータ構造の1つに :class:`dict` (辞書) があります。
:class:`dict` は別名マッピングとも呼ばれ、キーに対して値を紐付けて登録することができます。

.. code-block:: pycon

  >>> d = {"one": 1, "two": 2}
  >>> d["three"] = 3
  >>> d["one"]
  1
  >>> d["zero"]
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  KeyError: 'zero'

上記の例の最後のように、存在しないキーを参照すると例外が発生します。

これを踏まえて、ある文字列中にそれぞれの文字が何回出現したかを数える
プログラムを書いてみましょう。

.. code-block:: python

  s = "abrakadabra"

  d = {}
  for c in s:
      # d[c] += 1 としたいが、これだと最初に代入するときにエラーになる
      d[c] = d.get(c, 0) + 1

存在しないキーを参照した時のことをいちいち考えて書かないといけないので面倒です
(間違いが多くなります)。

:class:`defaultdict` を使えばすっきり書けます。

.. code-block:: python

  from collections import defaultdict

  s = "abrakadabra"

  d = defaultdict(int)
  for c in s:
      d[c] += 1

:mod:`collections` モジュールに :class:`defaultdict` が追加されたのは
Python 2.5 からなので、 Python 2.4 では使えません。

.. note::

   `Python 2.4 で使える defaultdict の実装
   <http://code.activestate.com/recipes/523034-emulate-collectionsdefaultdict/>`_
   もあります。
