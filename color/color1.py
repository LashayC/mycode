import crayons

#print redstring in red
print(crayons.red('red string'))

#red white and blue text
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

#disable crayons package
crayons.disable()

#this line shoouldn't have color bc crayons disabled
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

#enable crayons package
crayons.DISABLE_COLOR = False

#this line will print color with crayons enabled
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

#print red string in red and bold
print(crayons.red('red', bold = True))

# print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))
