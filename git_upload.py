from github import Github

access_token = "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"
g = Github(access_token)
user = g.get_user()
# 레포지토리 연결 확인
repo = g.get_repo("etlers/fileload")
# 레포지토리 컨텐츠 목록
contents = repo.get_contents("")
# 이후 파일 존재여부를 판단하기 위한 파일 목록 저장. update or create
all_files = []
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

def upload_file(upload_file):
    # 업로드할 파일을 읽어들임
    with open(upload_file, 'r') as file:
        content = file.read()

    # 지정한 파일을 지정한 경로로 업로드
    git_prefix = 'monitoring/'
    git_file = git_prefix + upload_file
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="main")
        print(git_file + ' CREATED')


list_file = [
    "file_20210719.csv","file_20210720.csv","file_20210721.csv",
]
for file_name in list_file:
    upload_file(file_name)