# Automates the compiling and clean up of the directories.
#
# Author: Alexander Roth
# Date:   2015-01-06

.PHONY: compile
compile:
	javac Java/*.java

.PHONY: clean
clean:
	rm -f Java/*.class Python/*.pyc *~

.PHONY: all
all: clean compile
