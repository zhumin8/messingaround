import pip
packages=pip.get_installed_distributions()
for row in packages:
    print row
