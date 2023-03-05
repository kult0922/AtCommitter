# AtCommitter

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
  "extension": "cpp",
  "submittion_time_commit": false
}
```
If submittion_time_commit is true, the date and time of the commit will be the date of submission.

3. Run after contest and sync code with Github
```
Python3 abc290
```
