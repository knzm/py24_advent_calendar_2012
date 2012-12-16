:orphan:

.. _ubuntu-deadsnakes:

Ubuntu で Python 2.4 をインストールする方法
==================================================

Ubuntu も人気のある Linux ディストリビューションです。
デスクトップからサーバまで幅広い用途に使われています。
Ubuntu は CentOS とは異なり、比較的早いペースで新しいリリースが行われ、
収録されているソフトウェアのバージョンも新しめのことが多いです。

2010年4月にリリースされた Ubuntu 10.04 LTS (コードネーム Lucid Lynx) からは
Python 2.6 が標準となり、 Python 2.4 と Python 2.5 が公式のリポジトリで
提供されなくなりました。そして現在、2013年4月に間もなくサポート期間が終了する
8.04 LTS (コードネーム Hardy Heron) サーバ版を除き、サポートされている
すべてのリリースで利用できる Python のバージョンは 2.6 以降となっています。

開発環境として Ubuntu を使用している場合、テストのために Python 2.4
や Python 2.5 を動かしたいことがあります。
Launchpad の `Old and New Python Versions
<https://launchpad.net/~fkrull/+archive/deadsnakes>`_ PPA では、
そうした用途のために Ubuntu の各リリースに対して
2.4 以降のすべてのバージョンの Python が提供されています。

以下の手順で Python 2.4 をインストールすることができます。

::

  $ sudo add-apt-repository ppa:fkrull/deadsnakes
  $ sudo apt-get update
  $ sudo apt-get install python2.4

.. warning::

   - このリポジトリは個人の開発者が管理しているもので、一切の保証はありません
   - 提供されているバージョンは最新とは限りません。
     特に、すべてのセキュリティ修正が適用されるわけではないので、
     実運用で使用することは避けるべきです。
