from github import Github
import urllib

access_token = "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"
g = Github(access_token)
user = g.get_user()

repo = g.get_repo("etlers/fileload")

contents = repo.get_contents("")
all_files = []
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        fnm = str(file).replace('ContentFile(path="','').replace('")','')
        all_files.append(fnm)
        if "fld_test/csv_file.csv" not in fnm: continue
        file_info = repo.get_contents(urllib.parse.quote(file_content.path), ref="main")
        print(file_info.download_url)

# for fnm in all_files:
#     if "fld_test/csv_file.csv" not in fnm: continue
#     print(fnm)