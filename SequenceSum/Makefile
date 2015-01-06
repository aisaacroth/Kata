# Automates the compiling and clean up of the directories.
#
# Author: Alexander Roth
# Date:   2015-01-06

.PHONY: compile
compile:
	javac Java/*.java

.PHONY: clean
clean:
	rm -rf Java/*.class Python/*.pyc *~ Python/__pycache__/

.PHONY: all
all: clean compile
