# 車窓からのTDD with Python and IntelliJ IDEA

TDDの古典教材「[車窓からのTDD](https://objectclub.jp/technicaldoc/testing/stack_tdd.pdf)」を、PythonとIntelliJ IDEAで実習します。

## 環境構築 (macOS)

### PyEnvのインストール

```
# https://github.com/pyenv/pyenv
% brew install pyenv

pyenv install --list
# 最新のstable版をinstall
pyenv install 3.12.3

# installされているpythonを確認
pyenv versions

# shellで必要な設定を書き込む
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### プロジェクト作成

```
% cd /path/to/project
% git init python_tdd_stack
% cd python_tdd_stack

# pythonのversionを指定
% pyenv local 3.12.3

# pythonの仮想環境を作る
% python -m venv .venv --prompt tdd_stack
% source .venv/bin/activate

# .gitignoreを取得
% curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore > .gitignore

# pyenvのmetafileをignoreする
% echo '.python-version' >> .gitignore

# LICENSEを取得（MIT LICENSE）→ {{year}} と {{ organization }} を書き換える
% curl https://raw.githubusercontent.com/licenses/license-templates/master/templates/mit.txt > LICENSE
% git add .
% git ci -m ':one: First commit'
```

### IntelliJ IDEAの準備
- プラグインをインストール
    - Python
    - GitHub Copilot
- `.gitignore`
    - [Markdown | IntelliJ IDEA ドキュメント](https://pleiades.io/help/idea/markdown.html#preview)
    - [gitignore/Global/JetBrains.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore)
    - [JetBrains IDE（IntelliJ IDEAなど）を使う時のgitignoreについて #IntelliJ - Qiita](https://qiita.com/aki3061/items/1f668dd0d1bee15b56f0)
