:orphan:

.. _centos-epel:

CentOS 5 で新しいバージョンの Python を使いたい場合
============================================================

CentOS は代表的な Linux ディストリビューションの一つで、
Red Hat Enterprise Linux と互換性があるためサーバ用途では
広く使われています。
元がエンタープライズ向けのためどちらかというと保守的で、
収録されているソフトウェアのバージョンも最新のものではなく
少し古いものが選ばれていることが多いです。

Python もその一つで、 CentOS 5 では Python 2.4 が標準インストールされます。
CentOS の最新は CentOS 6 ですが、 2011年7月に CentOS 6 がリリースされるまでは
CentOS 5 が最新でした。そのため今でも数多くのサーバが CentOS 5 で動いており、
まだまだ現役のリリースと言えます。

CentOS 5 では Python 2.4 を使い続けるしかないのでしょうか?
意外と知られていないことですが、 EPEL という外部リポジトリを利用することで
CentOS 5 でも Python 2.6 が使えるようになります。

EPEL を追加する
------------------------------

1. Fedora Project のサイトから EPEL の RPM パッケージをダウンロードしてインストールします。

::

  # wget http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
  # rpm -Uvh epel-release-5-4.noarch.rpm

.. note::

   - 32bit の場合は ``x86_64`` の部分を i386 に読み替えてください
   - ``release-5-4`` の数字部分は将来更新されるかもしれません。
     ダウンロードに失敗した場合は新しいバージョンがリリースされていないかどうか
     確認してみてください。
   - Web 上の過去の記事等では download.fedora.redhat.com が紹介されている
     ことがありますが、現在はドメインが dl.fedoraproject.org に変更されています。

2. :file:`/etc/yum.repos.d/epel.repo` をエディタで開いて、 ``enabled=1``
となっている箇所を以下のように ``enabled=0`` に変更します。これによって、
普段は EPEL を無効にしておき、必要な時だけ使うということができます。

::

  [epel]
  ...
  enabled=0

Python 2.6 をインストールする
------------------------------

yum コマンドを使って python26 パッケージをインストールします。
必要なら python26-devel などの関連するパッケージも同様に
インストールしてください。

::

  # yum install python26 --enablerepo=epel

python26 パッケージは、既存の python パッケージを置き換えるのではなく、
Python 2.4 と Python 2.6 を共存させることを可能にします。
そのため python26 をインストールしても Python 2.4 は今まで通り使えます。

.. warning::

  EPEL リポジトリを無効にしているため yum update では更新されません。
  したがって、セキュリティアップデートがないかどうか定期的に確認して、
  手動でパッケージを更新するようにしてください。
