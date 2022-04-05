#! /usr/bin/env python3


def main():
    mods = 'CSC1009'

    # Map -> will use matchcase if 3.10 is supported
    if mods.upper() == 'CSC1006':
        mapped = 'Maths 2'
    elif mods.upper() == 'CSC1007':
        mapped = 'Operating System'
    elif mods.upper() == 'CSC1008':
        mapped = 'Data Structure'
    elif mods.upper() == 'CSC1009':
        mapped = 'Object-Oriented Programming'
    elif mods.upper() == 'CSC1010':
        mapped = 'Computer Network'
    else:
        mapped = 'Unknown Mod'
        
    print(f'{mapped}')

if __name__ == "__main__":
    main()
