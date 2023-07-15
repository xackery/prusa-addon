VERSION ?= 2.0.5

comma := ,
COMMA_VERSION := $(subst .,${comma} ,${VERSION})

build:
	@echo "build: packing and building"
	mkdir -p bin
	-rm -rf bin/*
	cd /src/prusa && make build-windows && cp bin/prusa-win-x64.exe prusa.exe
	sed -i '' 's/"version": (1, 0, 0),/"version": (${COMMA_VERSION}),/' __init__.py
	mkdir -p bin/prusa-addon
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
	cp prusa.exe LICENSE README.md *.py bin/prusa-addon
	cp -r converter common auto_load bin/prusa-addon
	cd bin && zip prusa-${VERSION}.zip prusa-addon
	rm -rf bin/prusa-addon
	sed -i '' 's/"version": (${COMMA_VERSION}),/"version": (1, 0, 0),/' __init__.py

build-darwin:
	@echo "build-darwin: packing and building"
	@mkdir -p bin
	cd /src/prusa && make build-darwin
	cp /src/prusa/bin/prusa-darwin-x64 prusa-darwin