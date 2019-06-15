OPENAPI_YAML = yaml/hep-openapi-v1.yaml

all:rest.py rest.java-retrofit2 rest.php rest.swift
	@echo "Generate success"

rest.py:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l python -o sdks/python -c codegen-config/config-python.json
	@make -C sdks/python/post_codegen

rest.java-retrofit2:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l java -o sdks/java-retrofit2 -c codegen-config/config-java-retrofit2.json --model-package org.newtonproject.hep.rest.models 

rest.php:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l php -o sdks/php -c codegen-config/config-php.json

rest.swift:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l swift4 -o sdks/swift -c codegen-config/config-swift.json
