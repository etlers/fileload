# PyGithub module
from github import Github

access_token = "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"
g = Github(access_token)
user = g.get_user()
# print(user.name)
# print(user.login)
# print(user)
repo = g.get_repo("etlers/shell")
contents = repo.get_contents("")
all_files = []
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
target_dir = "rsync/dest"
max_fnm = ""
for full_name in all_files:
    if target_dir not in full_name: continue
    fnm = full_name.split("/")[full_name.count("/")]
    if fnm > max_fnm:
        max_fnm = fnm
print(max_fnm)
# for repo in g.get_user().get_repos(""):
#     print(repo.get_contents)
#     if repo.name != "kotlin": continue
#     # repo.edit(has_wiki=False)
# # login = user.login
# # print(login)
#     all_files = []
    # contents = repo.get_contents("")
#     # for content in contents:
#     #     print(content.type, content)
#     while contents:
#         file_content = contents.pop(0)
#         if file_content.type == "dir":
#             contents.extend(repo.get_contents(file_content.path))
#         else:
#             file = file_content
#             all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
    # print(all_files)

# with open('file.txt', 'r') as file:
#     content = file.read()
# print(content)
# Upload to github
# git_prefix = 'fileload/'
# git_file = git_prefix + 'file.txt'
# if git_file in all_files:
#     contents = repo.get_contents(git_file)
#     repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
#     print(git_file + ' UPDATED')
# else:
#     repo.create_file(git_file, "committing files", content, branch="master")
#     print(git_file + ' CREATED')