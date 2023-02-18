## AZTools Shelf

BlenderにMayaライクなシェルフを追加するアドオン<br>

<br>

## サポート環境

Blender3.4.1以降<br>

<br>


## インストール方法

### ①ZIPのインストール方法

右上のCodeをクリックしてDownload ZIP<br>
<img width="400" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/28b2cbe0-765e-8aad-753c-1e6bdb8d28d2.png">

zipをダウンロードしてBlenderの環境設定からインストールボタンを押して、<br>
先ほどダウンロードしたzipファイルを指定してください<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/a46099e1-4d81-a5a0-c247-36b2821ce30b.png)



<br>

### ②おすすめのインストール方法

ご自分のBlenderのaddonフォルダーにこのリポジトリをクローンしてください。<br>
git pullで常に最新版更新できます。

<br>


## 使い方<br>
環境設定からアドオンを有効化<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/aa79819f-ef5e-f0ec-004f-21d4d80dbebd.png)

メニューにAZToolsのタブが追加されます。<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/75d0499b-29ec-7d0f-69f4-59004902d005.png)

こちらからAZTools Shelfにアクセス<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/10acc8eb-80e0-a3be-dbdb-92aacb887dc2.png)

Openボタンを押すとシェルフフォルダが開きます。<br>
<img width="800" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/5cd47543-6860-02c6-ba76-d97511258a42.png">


こちらに
```
shelf_グループ名_スクリプト名.py
```
でスクリプトを追加すると<br>
シェルフにスクリプトが追加されます。

こちらは
**shelf_object_selectOnlyMesh.py**
で追加した様子。
ファイル名はキャメル記法で命名すると、<br>
自動的にボタンの名前にアッパースネーク記法（_はスペース）で表示されます。<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/29192cb4-0ab1-33eb-d19f-db07fe21e2fe.png)

ただしuvと名前の付くものについては
```
shelf_uv_スクリプト名.py
```
イメージエディターに表示されます。<br>
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/704965/fc70898f-84b4-c6f3-dafc-0e2e42691ea4.png)
