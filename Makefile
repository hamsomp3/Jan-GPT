# Default SHELL and PATH for Unix-like systems (Mac/Linux)
SHELL := /bin/bash
PATH := .venv/bin:$(PATH)



# Target for Unix-like systems
install-unix:
	@( \
		if [ ! -d .venv ]; then python3 -m venv --copies .venv; fi; \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
	)

local-setup-mac: install-unix

# Target for Windows
SHELL_WIN := cmd.exe
PATH_WIN := .venv/Scripts:$(PATH)
ACTIVATE_VENV_WIN := .\\venv\\Scripts\\activate

install-windows:
	if not exist ".venv" python -m venv --copies .venv
	.venv/Scripts/python.exe -m pip install -qU pip
	.venv/Scripts/pip install -r requirements.txt

local-setup-windows: install-windows

activate-windows:
	@cmd.exe /K .venv\Scripts\activate.bat

activate-unix:
	@echo Run 'source .venv/bin/activate' to activate the virtual environment

chroma-setup:
	docker build -t mi-aplicacion .

chroma-run:
	docker run -p 8000:8000 mi-aplicacion

#STREAMLIT_APP := codigo.py
STREAMLIT_APP := codigo.py
STREAMLIT_APP1 := chatbot.py
STREAMLIT_APP2 := chatbot2.py

stream:
	streamlit run $(STREAMLIT_APP)

stream1:
	streamlit run $(STREAMLIT_APP1)

stream2:
	streamlit run $(STREAMLIT_APP2)