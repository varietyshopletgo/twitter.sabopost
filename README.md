# サボポスト
- 毎日0時に令和市の今日の記念日の、文章と画像を自動生成してtwitterに投稿します。  
- レンタルサーバを使わずにiPadで完結できるようにつくりました。  

 ## 機能
 ① AdaloのAPIを使ってホームページに入力された記念日の情報を呼び出します。  
 ② 「今日はどんな日」の画像を自動生成します。  
 ③ 投稿用の文章を作成します。  
 ④ ②と③を合わせて毎日0時にtwitterへ投稿します。  
   
 ## 必要なもの  
 ### 環境  
  - iPad(iPhoneでも可)
  - アプリ： [a-Shell](https://holzschu.github.io/a-Shell_iOS/)
  - アプリ： [ショートカット](https://support.apple.com/ja-jp/guide/shortcuts/welcome/ios)
  
 ### 実行ファイル  
  - `dailyTweet.py`  
  
 ### フォント関連  
  - NotoColorEmoji.ttf  
  - NotoSansJP-Bold.otf  
  - NotoSansJP-Medium.otf  
  ⇒それぞれダウンロードして、`dailyTweet.py`と同じ階層においてください  
 
 ### 画像  
  - 背景画像`bg.jpg`  （1200px×630px推奨）  
  
 ### 実行手順  
 ① [a-shell](https://holzschu.github.io/a-Shell_iOS/)のフォルダに`dailyTweet.py`をコピーする  
 ② [ショートカット](https://support.apple.com/ja-jp/guide/shortcuts/welcome/ios)のオートメーション機能で0:00に`dailyTweet.py`が実行されるようにコマンドを入力する    
 ![165251477_150396266967705_1798557284637358125_n](https://user-images.githubusercontent.com/59709026/112727988-6d6a8400-8f68-11eb-8ff1-a3cfc9d6daba.jpg)

 ③「実行の前に尋ねる」をオフ    
![163759513_220889889832935_7060433481708031965_n](https://user-images.githubusercontent.com/59709026/112727959-5166e280-8f68-11eb-8426-6ca67c8b5464.jpg) 
 
 
 これで、自動的にツイートされます。
 
 
 
 
