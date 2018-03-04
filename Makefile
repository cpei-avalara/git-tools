prefix = /usr/local
bindir = $(prefix)/bin

SCRIPTS = \
	git-edit \
	git-fixup \
	git-mark

all:

install: all
	for script in $(SCRIPTS); do \
		install -m 755 $$script $(bindir)/; \
	done
	ln -sf git-mark $(bindir)/git-unmark
