#pip install GitPython
from git import Git, Repo

repo = Repo.init('.')  #初始化

#顯示狀態
status = repo.git.status()
print(status)

#下載專案檔案到指定路徑
#Repo.clone_from('https://github.com/tu202/mypython20240620.git', './download')

for commit in repo.iter_commits():  #查看上傳歷史紀錄
    print(commit)


#準備要上傳的路徑
local_repo_path = '.'  #本地路徑
remote_repo_url = 'https://github.com/mry88312/PYTHON_CLASS.git' #遠端路徑

# 打開本地暫存庫
repo = Repo(local_repo_path)

#準備要上傳的檔案
repo.index.add(['123.py'])  #檔案
repo.index.commit('4nd')  #註解


# 使用Git對象進行檔案推送上傳
g = Git(repo.working_dir)
g.push(remote_repo_url)
