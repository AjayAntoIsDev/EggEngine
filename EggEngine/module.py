'''
Part of EggEngine.

Usage: 'from EggEngine import module' or 'import EggEngine.module'

Includes functions to install dependencies for Engine as well as update every Python package/module installed.

Made by @eggnaut
'''

import sys
import subprocess as sp
import platform as pm

def dependencies(pip: str | None) -> None:
    '''
    Installs the required modules/dependencies that this engine/framework requires.

    Args:
        pip (str | None, optional): for macOS: pip3, for Windows: pip, this is a terminal/shell command
    '''
    
    if pip:
        try:
            sp.call(f'{pip} install pygame', shell = True)
            sp.call(f'{pip} install cryptography', shell = True)
            sp.call(f'{pip} install pillow', shell = True)
        except:
            print(f'\nEggEngine.module.dependencies() was unable to install dependencies.\nError: {pip} is not a valid shell command.\nPlease make sure the pip type (pip or pip3) provided is correct.\n')
            sys.exit()
    else:
        if pm.system() == 'Windows':
            sp.call('pip install pygame', shell = True)
            sp.call('pip install cryptography', shell = True)
            sp.call('pip install pillow', shell = True)
        elif pm.system() == 'Darwin' or pm.system() == 'Linux':
            sp.call('pip3 install pygame', shell = True)
            sp.call('pip3 install cryptography', shell = True)
            sp.call('pip3 install pillow', shell = True)

def updateAll(pip: str | None) -> None:
    '''
    Updates all installed modules without the hassle of this once tedious task.

    Args:
        pip (str | None, optional): for macOS: pip3, for Windows: pip, this is a terminal/shell command
    '''
    
    if pip:
        try:
            sp.call(f'{pip} list --outdated > outdated.txt', shell = True)
        except:
            print(f'\nEggEngine.module.updateAll() was unable to update modules.\nError: {pip} is not a valid shell command.\nPlease make sure the pip type (pip or pip3) provided is correct.\n')
            sys.exit()
    else:
        if pm.system() == 'Windows':
            sp.call('pip list --outdated > outdated.txt', shell = True)
        elif pm.system() == 'Darwin' or pm.system() == 'Linux':
            sp.call('pip3 list --outdated > outdated.txt', shell = True)

    with open('outdated.txt', 'r') as file:
        file.readline()
        file.readline()

        while True:
            package = file.readline()

            if package.split():
                name = package.split()[0]
                if pip:
                    sp.call(f'{pip} install --upgrade {name}' , shell = True)
                else:
                    if pm.system() == 'Windows':
                        sp.call('pip install --upgrade {name}' , shell = True)
                    elif pm.system() == 'Darwin' or pm.system() == 'Linux':
                        sp.call('pip3 install --upgrade {name}' , shell = True)
                        
            elif not package:
                break

        file.close()