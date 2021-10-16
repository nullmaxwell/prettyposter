.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROFILE = default
PROJECT_NAME = prettyposter
PYTHON_INTERPRETER = python3

ifeq (,$(shell which pyenv))
HAS_PYENV=False
else
HAS_PYENV=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies.
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Delete all compiled Python files and output files.
clean:
	rm -rf output/*
	rm -rf .pytest_cache
	find . -type d -name "cache" -delete
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	black src

## Set up python interpreter environment.
create_environment:
ifeq (True,$(HAS_PYENV))
	@echo ">>> Detected pyenv, creating virtualenv..."
ifeq (3,$(findstring 3,$(PYTHON_INTERPRETER)))
	pyenv virtualenv 3.9.7 $(PROJECT_NAME)
else
	pyenv virtualenv 2.7.18 $(PROJECT_NAME)
endif
	@echo ">>> New virtualenv created. Activate with:\nmake init_environment"
else
	$(PYTHON_INTERPRETER) -m pip install -q virtualenv virtualenvwrapper
	@echo ">>> pyenv not installed.\nPlease install pyenv and attempt again.\n
endif

## Initializes the created pyenv virtualenv in the local directory.
init_environment:
	pyenv virtualenv local $(PROJECT_NAME) && pyenv shell $(PROJECT_NAME)

## Removes all installed packages from the installed pyenv.
clean_environment:
	pip freeze | xargs pip uninstall -y

## Remove the virtual environment
remove_environment:
	pyenv uninstall $(PROJECT_NAME)

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

## Tests python source code
test_src:
	pytest tests/*

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
