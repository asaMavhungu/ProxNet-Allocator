VENV_DIR := venv
REQUIREMENTS_FILE := requirements.txt

install: venv
	. $(VENV_DIR)/bin/activate; pip3 install -Ur $(REQUIREMENTS_FILE)

venv:
	test -d $(VENV_DIR) || virtualenv $(VENV_DIR)

activate:
	@echo "Activating virtual environment..."
	@. $(VENV_DIR)/bin/activate; exec $$SHELL

clean:
	rm -rf $(VENV_DIR)
	find -iname "*.pyc" -delete