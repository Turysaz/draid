#!/bin/sh

# synchronises the directories

touch /drive/one/dailytouch
touch /drive/two/dailytouch

echo "backup at" > /logdir/bkuprpt
date >> /logdir/bkuprpt

python3 ./mkbkup.py /drive/one/ /drive/one_mirror/ >> /logdir/bkuprpt
python3 ./mkbkup.py /drive/two/ /drive/two_mirror/ >> /logdir/bkuprpt
