from github import Github

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
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
print(all_files)

with open('csv_file.csv', 'r') as file:
    content = file.read()
print(content)
# Upload to github. if folder not exists then create
git_prefix = 'fld_test/'
git_file = git_prefix + 'csv_file.csv'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="main")
    print(git_file + ' CREATED')