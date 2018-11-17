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
	@echo -e "\t - run-server : Runs the flask server"
	@echo -e "\t - publish: publishes docs to surge"
	@echo 
	@echo "Everything else (make html, make latex, etc) are passed directly as commands to sphinx"

publish:
	@make html
	@echo 
	@echo "Publishing....."
	@echo "Note that you need to have `surge` installed and on your PATH."
	@echo "And you also need to add the domain you want to docs/CNAME"
	@echo 
	@cd docs && cp ./CNAME build/htm && surge ./build/html


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: 
	@cd docs && $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)