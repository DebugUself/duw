# -*- coding: utf-8 -*-
'''inv matter for auto pub. 101.camp
'''

__version__ = 'blog101CAMP v.220925.1642'
__author__ = 'Zoom.Quiet'
__license__ = 'CC-by-nc-nd@2022.9'

#import io
import os
#import re
import sys
import time
#import datetime
#import json
#import marshal as msh
#import subprocess
#import logging
from textwrap import dedent as dedentxt

#import sys
import logging
#logging.basicConfig()
logging.basicConfig(level=logging.CRITICAL)
_handler = logging.StreamHandler()
_formatter = logging.Formatter("[%(levelname)s]%(asctime)s:%(name)s(%(lineno)s): %(message)s"
                #, datefmt='%Y.%m.%d %H:%M:%S'
                , datefmt='%H:%M:%S'
                )
_handler.setFormatter(_formatter)
LOG = logging.getLogger(__name__)
#LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)  
LOG.propagate = False

LOG.addHandler(_handler)
#LOG.debug('load LOG level')







from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)
from pprint import pformat

#import platform
#os_name = platform.system()
#del platform

#import subprocess





from invoke import task
#from fabric.context_managers import cd

from invoke import task
#import requests
from icecream import install
install()
ic.configureOutput(prefix='ic|>')


CAMPROOT = "/opt/scm/srv/pol4du/_sites/du" #os.environ.get("DU19SRC_ROOT")
CSITES = {'duw':{'ori':'br_duw_pub'
                , 'src':'br_DUW'
                , 'ghp':'ghp_duw'
                }
        }

AIM = 'site'
_TRIP = '_trigger'
_TOBJ = 'deploy.md'
TRIGGER = 0


@task 
def ver(c):
    '''echo crt. verions
    '''
    print('\n\t powded by {}'.format(__version__))


#   support stuff func.
def cd(c, path2):
    os.chdir(path2)
    print('\n\t crt. PATH ===')
    c.run('pwd')

#@task 
def ccname(c):
    c.run('cp CNAME %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')

#@task 
def sync4media(c):
    c.run('cp -rvf img %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')


#@task 
def pl(c, site):
    '''$ inv pl [101|py] <- pull all relation repo.
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    if site:
        #pp(CSITES[site])
        
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['gl'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
    else:
        ver(c)


@task 
def pl(c, site):
    '''pull all necessary change AT FIRST...
    '''
    _src = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
    cd(c, _src)
    #c.run('git st')
    c.run('git pl')

    _src = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
    cd(c, _src)
    #c.run('git st')
    c.run('git pl')

    _src = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    cd(c, _src)
    #c.run('git st')
    c.run('git pl')

    ver(c)
    return None

    chktri(c)

#@task 
def sync(c, site, crtweek):
    '''$ inv sync duw <- auto cp all need .md from DUW branch
    删除还没完成记要的准备模板 *_draft.md
    '''
    _src = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
    print(_src)

    _self = '%s/%s/docs'%(CAMPROOT, CSITES[site]['ori'])
    print(_self)
    #return None
    cmd_cp = 'cp -f %s/*.md %s/'%(_src, _self)
    print(cmd_cp)
    c.run(cmd_cp)

    cmd_cpd = 'cp -rf %s/20* %s/'%(_src, _self)
    print(cmd_cpd)
    c.run(cmd_cpd)

    cmd_rm = 'find %s -name "*_draft.md"  | xargs rm -vf '%( _self)
    print(cmd_rm)
    c.run(cmd_rm)

    cmd_rnf = f'cp -vf {_src}/{crtweek}w_draft.md {_self}/{crtweek}w.md'
    print(cmd_rnf)
    c.run(cmd_rnf)
    
    cmd_mvs = f'mv -v {_src}/{crtweek}w_draft.md {_src}/{crtweek}w.md'
    print(cmd_mvs)
    c.run(cmd_mvs)

    #ver(c)
    return None

    



@task 
def bu(c, site):
    '''$ inv bu duw <- usgae MkDocs build AIM site
    '''
    reidx(c, site)
    c.run('mkdocs -q build', hide=False, warn=True)

    c.run('pwd')
    ver(c)
    return None

#@task 
def pu(c, site):
    '''push original branch...
    '''
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                        , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
            '"deploy fresh %s by MkDocs (at %s)"'%(site,_ts)
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#   'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '
#@task 
def gh(c, site):
    '''$ inv gh [101|py] <- push gh-pages for site publish
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    
    ccname(c)
    #sync4media(c)
    
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                        , str(time.time()).split('.')[1][:3] )
    
    _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
    cd(c, _aim)
    #os.chdir(AIM)
    #with cd('site/'):
    #c.run('pwd')
    c.run('ls')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
            '"pub.(%s) gen. by MkDocs as invoke (at %s)"'%(site, _ts)
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#@task
def chktri(c, site):
    '''check trigger obj. set TRIGGER switch
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    _aimp = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
    #ic(_aimp)
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _p2tri =  '%s/%s'%(_aimp, _TRIP)
    #print(_p2tri)
    #print(os.listdir(_path))
    #print(type(os.listdir(_path)))
    if _TOBJ in os.listdir(_p2tri):
        print('\n\tTRIGGERed by %s exist'% _TOBJ)
        TRIGGER = 1
    else:
        print('\n\tTRIGGER obj. -> %s ~> NOT exist\n\t CANCEL build...'% _TOBJ)
        TRIGGER = 0

    ic(open(f"{_p2tri}/deploy.md","r").read())
    return open(f"{_p2tri}/deploy.md","r").read()[:-1]

#@task
def recover(c,site):
    '''recover trigger state, by del TRIGGER obj.
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _from = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
    print(_from)
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _path =  '%s/%s'%(_from, _TRIP)
    #_path =  './%s'% _TRIP
    _obj =  '%s/%s'%(_path, _TOBJ)
    print(_obj)
    c.run('rm -vf %s'% _obj)
    c.run('ls -Aogh %s'% _path)
    
    cd(c, _from)
    c.run('git st')
    c.run('git fix "(pubDUW) recover trigger obj. wait NEXT deploy"')
    
    _self = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    print(_self)
    cd(c, _self)
    
    TRIGGER = 0
    print('TRIGGER obj. recover -> waiting human deploy again')


def _injector(aim, drug):
    '''inject drug into aim .md
    ::.
        <- here
    .::
    '''
    _TS = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                    , str(time.time()).split('.')[1][:3] )
    #print(aim,drug)
    _exp = ''
    _replace = 0
    for l in open(aim):
        #print(l)
        if '::.' == l[:-1]:
            print('start inject')
            _replace = 1
            _exp += l 
        elif '.::' == l[:-1]:
            _replace = 0
            _exp += "\n"+drug
            print(drug)
            _exp += '\n\n(auto index injected by %s) \n\n'% __version__
            _exp += l 
            print('end inject')
        else:
            if _replace:
                pass
            else:
                _exp += l 
            
    #print(_exp)
    open(aim,'w').write(_exp)
    return None


@task
def reidx(c, site):
    '''$ inv reidx duw <- re-build all index.md
    '''
    #global TRIGGER
    global _TRIP, _TOBJ

    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _crt = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    _doc = '%s/docs'%_crt
    #print(_doc)
    _lasted = []
    for root, dirs, files in os.walk(_doc):
        '''for d in dirs:
            pp(d)
        for f in files:
            pp(f)
        '''
        if len(dirs) > 0:
            #print('as startting...')
            continue
        else:
            pp(root)
            #print(root.split('/'))
            _sub = root.split('/')[-1]
            #pp(dirs)
            _idx = []
            for f in files:
                if 'index.md' == f:
                    pass
                else:
                    _md = "%s/%s"%(root,f)
                    #print(_md)
                    #print(f.split('-'))item
                    _item = '- [{}]({})'.format(open(_md).readlines()[0][1:-1]
                                    , f)
                    _idx.append(_item)

                    _fn = f.split('-')
                    _r2li = '- [{}]({}/{})'.format(open(_md).readlines()[0][1:-1]
                                    ,_sub
                                    , f)

                    _lasted.append((f[:3],_r2li))

            #pp(files)
            #pp(_idx)
            #pp(sorted(_idx,reverse=True))
            #re_idx = sorted(_idx,reverse=True)
            _aim = "%s/index.md"%root
            _injector(_aim, '\n'.join(_idx))
            #print('\n'.join(re_idx))
        #print('\n\tanothers levels...\n')




    #pp(_lasted)
    _top = 7
    _update = []
    
    #pp(sorted(_lasted,reverse=True)[:7])
    #pp(_lasted)
    for item in sorted(_lasted,reverse=True)[:7] : 
        _update.append(item[1])
    
    #pp('\n'.join(_update))
    #pp(_update)
    _aim = '%s/index.md'%_doc
    print('\n\t _injector', _aim)
    _injector(_aim, '\n'.join(_update))
    
    return None
    #print(os.listdir(_path))
    #print(type(os.listdir(_path)))
    if _TOBJ in os.listdir(_path):
        print('\n\tTRIGGERed by %s exist'% _TOBJ)
        TRIGGER = 1
    else:
        print('\n\tTRIGGER obj. -> %s ~> NOT exist\n\t CANCEL build...'% _TOBJ)
        TRIGGER = 0

@task 
def pub(c, site):
    '''$ inv pub duw <- auto deploy new site version base multi-repo.
    '''
    global TRIGGER
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    #pl(c, site)
    _crt = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    
    #pl(c, site)
    
    cd(c, _crt)
    _crtweek = chktri(c, site)
    #print(TRIGGER)
    ic(f"{_crtweek}w_draft.md")
    #return None
    
    if TRIGGER:
        print('auto deplo NOW:')
        #return None
        sync(c, site, _crtweek)
        bu(c, site)
        recover(c, site)
        pu(c, site)
        # ccname(c)
        # sync4media(c)
        gh(c, site)
    else:
        print('nothing need deploy')
    
    ver(c)
    return None



