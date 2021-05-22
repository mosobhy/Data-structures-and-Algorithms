"""
the outline of moving disks is:
1. Move a tower of height - 1 to a via pole using a final pole
2. Move the remaining disk to the final pole
3. Move the tower of height - 1 from a via pole to a final pole using the original pole

"""

def move(f, t):
    print(f'move disk from {f} to {t}')

def moveTower(height, fromPole, toPole, viaPole): # height: nubmer of diskt to move, f: from pole, t: final pole, v: via pole
    if height >= 1:
        moveTower(height - 1, fromPole, viaPole, toPole)
        move(fromPole, toPole)
        moveTower(height - 1, viaPole, toPole, fromPole)

if __name__ == '__main__':
    moveTower(2, 'A', 'C', 'B')
