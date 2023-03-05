# How to use
1. Create GitHub repository for Atcoder codes.
```
git clone git@github.com:kult0922/AtCommitter.git
mkdir codes
cd codes
git init
git remote add origin (your reopsitory)
(e.g. git remote add origin git@github.com:kult0922/AtCoderArchive.git)
```

2. Input your user name and code extension
``` conf.json
{
  "user": "Kurt_",
  "extension": "cpp"
}
```

3. Run after contest and sync code with Github
```
Python3 abc290
```
