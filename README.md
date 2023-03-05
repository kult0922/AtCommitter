# AtCommitter
[![GitHub](https://img.shields.io/github/license/kult0922/AtCommitter.svg)](https://img.shields.io/github/license/kult0922/AtCommitter)

## How to use
1. Create GitHub repository for Atcoder submission codes

2. Set up a remote repository in your local
```
git clone git@github.com:kult0922/AtCommitter.git
mkdir codes
cd codes
git init
git remote add origin (your reopsitory)
(e.g. git remote add origin git@github.com:kult0922/AtCoderArchive.git)
```

2. Input your user name and code extension in conf.json
``` conf.json
{
  "user": "Kurt_",
  "extension": "cpp"
}
```

3. Run after contest and sync code with Github
```
Python3 main.py abc290
```

## Environment
python v3.7~
```
pip install requests
```
