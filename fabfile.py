'''
Fabfile for auto deployment(DevOps).

@package       axneo.com.root
@subpackage    fab
@author        Axneo LLC <admin@axneo.com>
@copyright     Copyright (c) 2016, www.axneo.com
@license       www.axneo.com
@link          https://www.axneo.com
@version       Version 1.0.0
@filesource    fabfile.py
'''
'''
Import statements
'''
from fabric.api import *


'''
Get git status(short command)

@access    default
@since     1.0.0
'''
def stat():
    local('git status')


'''
Get git diff(short command)

@access    default
@since     1.0.0
'''
def diff():
    local('git diff')


'''
Add one/more new files to local git repo

@access    default
@since     1.0.0
'''
def git_add():
    local('git add .')


'''
Commit all to local repo.

@access    default
@since     1.0.0
'''
def commit():
    local('git commit -a')


'''
Amend last commit

@access    default
@since     1.0.0
'''
def commit_amend():
    local('git commit --amend')


'''
Get current tag.

@access    default
@since     1.0.0
'''
def get_tags():
    local('git describe --tags')


'''
Add tag for local repo.

@access    default
@param     tag_id
@since     1.0.0
'''
def tag(tag_id):
    local('git tag ' + tag_id)


'''
Pull latest code from remote.

@access    default
@since     1.0.0
'''
def pull():
    local('git pull')


'''
Push committed code to remote.

@access    default
@since     1.0.0
'''
def push():
    local('git push')


'''
Push tag to remote.

@access    default
@since     1.0.0
'''
def push_tags():
    local('git push --tags')


'''
Run pull on remote server.

@access    default
@since     1.0.0
'''
def run_pull():
    run('git pull')


'''
Change the head to another  local branch.

@access    default
@param     branch
@since     1.0.0
'''
def checkout(branch):
    local('git checkout ' + branch)


'''
Merge a given branch.

@access    default
@param     branch
@since     1.0.0
'''
def merge(branch):
    local('git merge ' + branch)


'''
Update a given local branch with upstream.

@access    default
@param     branch
@since     1.0.0
'''
def sync(branch):
    checkout(branch)
    pull()


'''
Repo deployment

@access    default
@since     1.0.0
'''
def sync_repo():
    checkout('master')
    git_add()
    commit()
    pull()
    push()