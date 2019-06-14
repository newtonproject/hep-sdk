OPENAPI_YAML = yaml/hep-openapi-v1.yaml

all:py java-retrofit2 rest.php rest.swift
	@echo "Generate success"

py:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l python -o python -c config-python.json

java-retrofit2:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l java -o java-retrofit2 -c config-java-retrofit2.json --model-package org.newtonproject.hep.rest.models 

rest.php:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l php -o php -c config-php.json

rest.swift:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l swift4 -o swift -c config-swift.json
