.. _with:

``with`` 構文が使えない
==============================

プログラミングでは、例えばファイルの :func:`!open` と :func:`!close` のように、対になる
処理がよく出てきます。

例外が発生した場合でも確実にファイルが閉じられるようにするには、
間の処理を :keyword:`try`-:keyword:`finally` で囲みます。

::

  f = open("input.txt")
  try:
      n = 0
      for line in f:
          n += int(line)
      print n
  finally:
      f.close()

でもこれだと、 :keyword:`try` と :keyword:`finally` がいくつも並んでいると
対応関係が分かりづらいですし、うっかり :func:`!close` し忘れてしまうかもしれません。

Python 2.5 以上 [*]_ では、 ``with`` 構文を使って
もっと簡単に書くことができます。

::

  with open("input.txt") as f:
      n = 0
      for line in f:
          n += int(line)
      print n

でも Python 2.4 では使えません。

.. [*] Python 2.5 では以下の 1行を書くことで使えるようになります。

       ::

         from __future__ import with_statement

       Python 2.6 からは普通に使えます。
