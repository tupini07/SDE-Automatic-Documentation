# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@echo Available commands:
	@echo 
	@echo --- help : displays this message
	@echo --- sphinx-help : displays all the targets that can be built with this make file
	@echo --- run-server : Runs the flask server
	@echo --- publish : publishes docs to surge
	@echo --- unpublish : deletes the page you hosted on the CNAME domain from surge servers
	@echo 
	@echo "Everything else (ake html, make latex, etc) are passed directly as commands to sphinx"

sphinx-help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


publish: html
	@echo 
	@echo ---------------------------------------------------------------
	@echo Publishing.....
	@echo Note that you need to have 'surge' installed and on your PATH.
	@echo And you also need to add the domain you want to docs/CNAME
	@echo ---------------------------------------------------------------
	@echo 
	cp docs/CNAME docs/build/html/ 
	surge docs/build/html


unpublish:
	@echo 
	@echo ---------------------------------------------------------------
	@echo Unpublishing.....
	@echo Note that you need to have 'surge' installed and on your PATH.
	@echo And you also need to add the domain you want to delete to docs/CNAME
	@echo ---------------------------------------------------------------
	@echo 
	cat docs/CNAME | surge teardown 



# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: 
	@# we're removing docs/build to en7sure that all the changes are loaded. Depending on OS this
	@# might not always be the case by default
	@rm -rf docs/build 
	@cd docs && $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)