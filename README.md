# morph_gui

GUIによる日本語の名詞のみを取り出すために形態素解析を行うためのツールです.  
PyQtを使用しています.  
  
複数のファイルを選択することができます．  
シェルにAliasを作って使ってください.  

例:
```zsh
alias morph_gui='python /Users/noriakioshita/Github/python/morph_gui/morphological_analysis_gui.py'
```

macのFinderのようにディレクトリを階層表示できないので,  
一旦ファイルを一つのディレクトリに入れて複数選択してください． 

## イメージ
<img src="/image/形態素解析するファイルを選択.png" width=420 height=310 alt="input">  
  
<img src="/image/ターミナル.png" width=620 height=180 alt="output">  

## オプション
品詞を指定することができます．(引数を指定しなければ名詞のみの形態素解析になります．)  
現在は,  
・副詞  
・動詞  
・形容詞  
・助詞  
・記号  
・助動詞  
・感動詞  
の解析が可能です．  

### 例えば．

```zsh
morph_gui 副詞 
morph_gui 動詞
morph_gui 形容詞
```
