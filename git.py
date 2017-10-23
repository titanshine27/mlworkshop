student@R2:~/Desktop/mlworkshop$ git init
Initialized empty Git repository in /home/student/Desktop/mlworkshop/.git/
student@R2:~/Desktop/mlworkshop$ status
unity-settings-daemon start/running, process 6681
student@R2:~/Desktop/mlworkshop$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	firstmodel.py
	gender.py
	iris.py

nothing added to commit but untracked files present (use "git add" to track)
student@R2:~/Desktop/mlworkshop$ git add --all
student@R2:~/Desktop/mlworkshop$ clear


student@R2:~/Desktop/mlworkshop$ git commit -m "first commit"
[master (root-commit) 5aa73d9] first commit
 3 files changed, 48 insertions(+)
 create mode 100644 firstmodel.py
 create mode 100644 gender.py
 create mode 100644 iris.py
student@R2:~/Desktop/mlworkshop$ git push https://github.com/titanshine27/mlworkshop.git master
Username for 'https://github.com': titanshine27
Password for 'https://titanshine27@github.com': 
Counting objects: 5, done.
Delta compression using up to 4 threads.

