OPENAPI_YAML = yaml/hep-openapi-v1.yaml

all:rest.py rest.java rest.php
	@echo "Generate success"

rest.py:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l python -o hep-rest.py -c config.json

rest.java:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l java -o hep-rest.java -c config.json 

rest.php:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l php -o hep-rest.php -c config.json
