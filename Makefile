VERSION ?= 1.0.0

comma := ,
COMMA_VERSION := $(subst .,${comma} ,${VERSION})

build:
	@echo "build: packing and building"
	mkdir -p bin
	-rm -rf bin/*
	sed -i '' 's/"version": (1, 0, 0),/"version": (${COMMA_VERSION}),/' __init__.py
	mkdir -p bin/prusa-addon
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
	cp LICENSE README.md *.py bin/prusa-addon
	cp -r converter common auto_load bin/prusa-addon
	cd bin && zip prusa-${VERSION}.zip prusa-addon
	rm -rf bin/prusa-addon
	sed -i '' 's/"version": (${COMMA_VERSION}),/"version": (1, 0, 0),/' __init__.py