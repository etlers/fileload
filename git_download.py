from github import Github
import urllib
import requests


access_token = "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"
g = Github(access_token)
user = g.get_user()

repo = g.get_repo("etlers/fileload")

contents = repo.get_contents("monitoring")
all_files = []
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        fnm = str(file).replace('ContentFile(path="','').replace('")','')
        all_files.append(fnm)
        # if "fld_test/csv_file.csv" not in fnm: continue
        # file_info = repo.get_contents(urllib.parse.quote(file_content.path), ref="main")
        # print(file_info.download_url, type(file_info.download_url))
        # r = requests.get(file_info.download_url, allow_redirects=True)
        # open('test.csv', 'wb').write(r.content)
last_fnm = all_files.pop()
print(last_fnm)
# for fnm in all_files:
#     if "fld_test/csv_file.csv" not in fnm: continue
#     print(fnm)