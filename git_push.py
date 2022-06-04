#!/usr/bin/env python3

from time import sleep
import os 


def git_commit():
    os.system('git status')
    sleep(3)
    os.system('git add .')
    sleep(3)
    os.system("git commit -m '*' " )
    sleep(3)
    os.system('git push')

    print('Code comitado com sucesso!')

if __name__=='__main__':
    git_commit()

