import subprocess as cmd

file = "csv_20210724.csv"
    

def git_push_automation():
    try:
        cp = cmd.run(file, check=True, shell=True)
        print("cp", cp)
        cmd.run(f"git add {cp}")
        cmd.run('git commit -m "git upload using command"', check=True, shell=True)
        cmd.run("git push -u origin main -f", check=True, shell=True)
        print("Success")
        return True
    except:
        print("Error git automation")
        return False


def git_push_checkout():
    cmd.check_output(f'git add .', shell=True)
    cmd.check_output('git commit -m "a commit"', shell=True)
    cmd.check_output("git push -u origin main -f", shell=True)

git_push_checkout()