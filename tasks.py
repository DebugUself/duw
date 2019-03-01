# -*- coding: utf-8 -*-

import time
from invoke import task


@task 
def hollo(c):
    c.run('echo hello', hide=False, warn=True)
    c.run('whoami')

@task 
def build(c):
    c.run('pwd')
    c.run('mkdocs build', hide=False, warn=True)

@task 
def pu(c):
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    c.run('git add .', hide=False, warn=True)
    c.run('git ci -am '
          '"inv(loc) MkDocs upgraded by DAMA (at %s)"'% _ts
                    , hide=False, warn=True)
    c.run('git pu', hide=False, warn=True)

@task 
def pub(c):
    build(c)
    pu(c)
