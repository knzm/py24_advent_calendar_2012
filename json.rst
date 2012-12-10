.. _json:

:mod:`json` モジュールがない
==============================

JSON は JavaScript Object Notation の略ですが、
最近では XML に代わる軽量データ記述言語として
JavaScript に限らず様々な言語で用いられることが増えてきました。

Python にも JSON を扱う標準ライブラリがありますが、これが追加されたのは
Python 2.6 です。

Python 2.4 では :mod:`simplejson` というサードパーティのライブラリを
使うことが一般的です。
サードパーティといっても Python 2.6 以降に含まれる :mod:`json` モジュールの
元になったものなので、モジュール名以外の使い方は共通になっています。
そのため、互換性を重視する場合は以下のような書き方をすることがあります。

::

  try:
      import simplejson as json
  except ImportError:
      import json

これによって、もし :mod:`simplejson` モジュールが存在したらそれを使い、
ない場合に :mod:`json` モジュールが存在したら (つまり Python 2.6 以降なら)
:mod:`json` モジュールを使う、ということが実現できます。

注意点として :mod:`simplejson` の最新版は Python 2.4 をサポート
していないため、インストールしようとするとエラーになります。
公式に Python 2.4 をサポートしている最終バージョンは 2.0.9 ですが、
2.3.3 までは Python 2.4 でも動作するようです。
インストールする際はこれらの古いバージョンを指定してください。

ちなみに、 JSON を扱うサードパーティのライブラリは :mod:`simplejson` 以外に

- `cjson <http://pypi.python.org/pypi/python-cjson/>`_
- `demjson <http://deron.meranda.us/python/demjson/>`_
- `jsonlib <https://launchpad.net/jsonlib>`_
- `jsonlib2 <http://code.google.com/p/jsonlib2/>`_

等がありますが、
`Python の JSONライブラリのパフォーマンステスト
<http://www.ianlewis.org/jp/python-json-library-perf-test>`_
によると、幸いなことにパフォーマンスを考慮しても :mod:`simplejson` を
使えば良いそうです。
