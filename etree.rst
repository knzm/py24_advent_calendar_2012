:orphan:

.. _etree:

:mod:`xml.etree` がない
==============================

Python で XML を扱う有名なライブラリの一つに :mod:`ElementTree`
があります。 :mod:`ElementTree` が Python 2.5 で標準ライブラリに
取り込まれたときに :mod:`xml.etree` という名前に変わりました。

:mod:`xml.etree` (または :mod:`ElementTree`) を使う場合、
実装やバージョンの違いによってモジュール名が異なるため、
様々な環境でも動くように最大限考慮すると
モジュールのインポートは非常に複雑になります。

::

  try:
      # lxml.etree
      from lxml import etree
  except ImportError:
      try:
          try:
              # cElementTree on Python 2.5+
              import xml.etree.cElementTree as etree
          except ImportError:
              # ElementTree on Python 2.5+
              import xml.etree.ElementTree as etree
      except ImportError:
          try:
              # cElementTree
              import cElementTree as etree
          except ImportError:
              # ElementTree
              import elementtree.ElementTree as etree


まず最初に `lxml <http://lxml.de/>`_ がインストールされているかどうかを
チェックしています。
:mod:`lxml` は高速で使いやすい XML ライブラリで、
ElementTree と互換性のある API を持っています。
そのため :mod:`lxml` がインストールされている環境ではそれを使います。

:mod:`ElementTree` には、動作がより高速な C 拡張版の :mod:`cElementTree`
があります。
標準ライブラリにもそれに対応して :mod:`xml.etree.ElementTree` と
:mod:`xml.etree.cElementTree` という 2 種類のモジュールがあります
(Python 3 では :mod:`xml.etree.cElementTree` が廃止されるそうです)。
これらを順にインポートできるかどうか試していき、最初に見つかった
ライブラリを使用します。

ただ、ここまでやるのは一部の本当に広く使われるソフトウェアだけで、
普段はそこまで気にすることは稀です。
個人的には、常に :mod:`lxml` を使えば良いと思います。

----

これだけだと Python 2.4 で :mod:`xml.etree` がなくても別に困らない、
という結論で終わってしまうので、 XML (と関連して HTML) を
パースする場合の tips を書いてお茶を濁します。

1) :mod:`xml.dom.pulldom` は使える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XML を処理する方式には DOM と SAX の2種類ありますが、このライブラリは
その両方の良いところを合わせたようなものです。
SAX イベントの途中で現在のノードから下の DOM ツリーを構築することが可能で、
XML から一部の情報を取り出す処理を簡単に書くことができます。

pulldom を使う例:

::

  from xml.dom import pulldom

  doc = pulldom.parse('items.xml')
  for event, node in doc:
      if event == pulldom.START_ELEMENT and node.tagName == 'item':
          if int(node.getAttribute('price')) > 50:
              doc.expandNode(node)
              print(node.toxml())

:mod:`xml.dom.pulldom` は Python 2.4 の標準ライブラリに含まれています。


2) :mod:`BeautifulSoup` は使える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

タグが閉じられていないような壊れた HTML は、純粋な XML パーザや
SGML パーザではうまく扱えません。
`BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/>`_ は、
ウェブブラウザと同じようにヒューリスティックを使用して
壊れた HTML も可能な限り修復してくれるので、
インターネットからダウンロードした大量の HTML をパースするような場合に
非常に重宝します。

さらに :mod:`lxml.html` と :mod:`BeautifulSoup` を組み合わせて使うための
:mod:`lxml.html.soupparser` というモジュールもあります。
HTML のスクレイピングをする場合に、これと後述する :func:`cssselect` を
使うのが最強の組み合わせだと思います。


3) :mod:`lxml.html` の :func:`cssselect` は使える
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:mod:`ElementTree` では XPath を使って DOM ツリーの中から特定のノードを
検索することができますが、 :mod:`lxml.html` の場合は XPath の代わりに
CSS でも検索ができます。内部では CSS を XPath に変換しているだけですが、
使ってみるととても使いやすいのでお勧めです。
