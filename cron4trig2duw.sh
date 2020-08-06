#! /bin/bash
export DU19SRC_ROOT="/opt/www/debuguself"
#echo $DU19SRC_ROOT
#=========================================================== var defines
VER="cron4trig2duw.sh v.200114.2200"
#VER="cron4trig2duw.sh v.190609.1803"
DATE=`date "+%y%m%d"`
#NOW=$(date +"%Y-%m-%d")
#PY=$( which python)
#/opt/bin/miniconda3/envs/py371/bin/pipenv
PIPENV=/opt/bin/miniconda3/envs/py371/bin/pipenv #$( which pipenv)
#VENV=`$PIPENV --venv`
VENV=/home/du19/.local/share/virtualenvs/br_duw_pub-XOQ-Lz1N
#echo $VENV
ACTIVATE=$VENV/bin/activate

GIT=$( which git)
#=========================================================== path defines
NOW=`date +"%y%m%d_%H%M%S"`
YEAR=`date +"%Y"`
MONTH=`date +"%m"`

export DU19SRC_ROOT=/opt/www/debuguself

ROOP=/opt/www/debuguself
SELF=$ROOP/br_duw_pub
AIMP=$ROOP/ghbr_logging_duw
ORIG=$ROOP/br_DUW
#TRIG=$ROOP/_trigger4deploy.log
TRIG=$ORIG/_trigger/deploy.md

LOGP=$AIMP/$YEAR/$MONTH
LOGF=$LOGP/$NOW.log
#=========================================================== action defines
echo $LOGP      #>> $LOGF 2>&1
mkdir -p $LOGP  #>> $LOGF 2>&1
#mkdir -p $LOGP  >> $LOGF 2>&1
#echo '' > $AIMP/$YEAR/.gitignore
#echo $TRIG

source $ACTIVATE
cd $SELF
$PIPENV run inv ver #>> $LOGF 2>&1
$PIPENV run inv pl duw

if [ -f $TRIG ];then
    echo "trigger @" `date +"%Y/%m/%d %H:%M:%S"`
    echo "github-hook->trigger exist, deploy NOW:-)"
    
    #echo $LOGF      >> $LOGF 2>&1
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"  >> $LOGF
echo "###::$VER crontab action 4 auto publish DUW"  >> $LOGF
echo "###::run@" `date +"%Y/%m/%d %H:%M:%S"` >> $LOGF
echo "<<<   trigger by $TRIG "  >> $LOGF
    
    #source $ACTIVATE
    #cd $SELF
    #$PIPENV run inv -l >> $LOGF 2>&1
    $PIPENV run inv pub duw >> $LOGF 2>&1

#    rm $TRIG
#    echo "<<<   clean $TRIG for next hooksrv act"  >> $LOGF

echo "###::end@" `date +"%Y/%m/%d %H:%M:%S"` >> $LOGF
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"  >> $LOGF

    cd $AIMP
    #pwd
    NOW=`date +"%Y-%m-%d %H:%M:%S"`
    $GIT add -f $YEAR/$MONTH/*.log
    $GIT new "(crontab) logging auto publish as $NOW"  #>> $LOGF 2>&1

echo "@ $NOW all deployed by $VER"
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

else

    NOW=`date +"%y%m%d.%H%M"`
    echo "$NOW ->trigger NOT exist, deploy later;-}"
    echo 
fi

#pwd

#=========================================================== action DONE
exit  0

