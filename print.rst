:orphan:

.. _print:

``print`` の出力先を変更する文法がダサい
==================================================

Python 2 系と Python 3 系で一番分かりやすい違いは ``print`` だと思います。

Python 2.4 では、文字列を出力する場合にこう書きます:

.. code-block:: pycon

  $ python2.4
  >>> print "Hello!"
  Hello!

非常に直感的ですね。
でも出力先をファイルにしたい場合はこんな風に書く必要があります:

.. code-block:: pycon

  >>> f = open("test.txt", "w")
  >>> print >> f, "Hello!"
  >>> f.close()

これは Python の他の文法からするとちょっと浮いた存在でした。

Python 3 から ``print`` は関数になったので、色々なパラメータを引数として渡せます。

.. code-block:: pycon

  $ python3
  >>> import sys
  >>> print("hello", "world", sep=', ', end='!?\n', file=sys.stderr)
  hello, world!?

Python 2.6 以降であれば、最初に次のような1行を書いておくことで ``print`` が関数になります。

.. code-block:: python

  from __future__ import print_function

でも Python 2.4 では使えません。
