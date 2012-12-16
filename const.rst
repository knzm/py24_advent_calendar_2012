:orphan:

.. _const:

``True`` や ``False`` が代入可能
========================================

Python 2.4 では True や False といった定数への代入は禁止されていません。
そのため、以下のような遊びができます。

::

  >>> True = False
  >>> True is False
  True
  >>> (True is False) is True
  False
  >>> (True is False) is False
  False

真と偽が等価だったり、真偽値なのに真でも偽でもない値が存在するという
何とも不条理な世界です。

残念ながら(?) Python 3 ではこれらの定数は代入不可能なキーワードになり、
代入しようとするとエラーになります。

::

  >>> True = False
    File "<stdin>", line 1
  SyntaxError: assignment to keyword

無事に世界の秩序は保たれました!
