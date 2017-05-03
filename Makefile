CWD := $(shell readlink -en $(dir $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))))

.PHONY: all
all: clean build

.PHONY: build
build: env
	cp plot.py plot
	chmod +x plot
	$(info built)

env:
	virtualenv env
	env/bin/pip install -r requirements.txt
	$(info created virtualenv)

.PHONY: freeze
freeze:
	env/bin/pip freeze > requirements.txt

.PHONY: clean
clean:
	@rm -rf **/*.pyc env plot
	$(info cleaned)
