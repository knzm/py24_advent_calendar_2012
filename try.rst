.. _try_except_finally:

``try-except`` と ``try-finally`` を1つの ``try`` にできない
============================================================

プログラムの中で例外が発生すると、通常それ以降のコードは呼ばれません。
それだと困る場合があるので、例外を処理するために ``try`` 文という仕組みが用意されています。
実際のコードの中では ``try`` と ``except`` (または ``try`` と ``finally``) を組み合わせて使います。

``except`` 節は例外が発生したときにだけ呼ばれます。

::

  while True:
      try:
          x = int(raw_input("Please enter a number: "))
          break
      except ValueError:
          print "Not a valid number.  Try again..."

``finally`` 節は例外が発生してもしなくても常に呼ばれます。

::

  f = open("input.txt")
  try:
      n = 0
      for line in f:
          n += int(line)
      print n
  finally:
      f.close()

Python 2.4 では、同じ ``try`` に ``except`` と ``finally`` を
両方指定することができないという制限があります。
そのため以下のような書き方は構文エラーになります。

::

  f = open(path, 'r')
  try:
      f.write('test')
  except IOError, (errno, msg):
      print 'Cannot write to %s: %s' % (path, msg)
  finally:
      f.close()

代わりに以下のように ``try`` を入れ子にします。

::

  f = open(path, 'w')
  try:
      try:
          f.write('test')
      except IOError, (errno, msg):
          print 'Cannot write to %s: %s' % (path, msg)
  finally:
      f.close()

別にどうってことはないのですが、インデントが深くなって行数が増えた分、
ソースコードがちょっとごちゃごちゃして読みにくくなってしまいました。

Python 2.5 以降にはそんな制限はありません。
