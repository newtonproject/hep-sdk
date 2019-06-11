OPENAPI_YAML = yaml/hep-openapi-v1.yaml

all:hep-rest.py hep-rest.java hep-rest.php
	@echo "Generate success"

hep-rest.py:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l python -o hep-rest.py -c config.json

hep-rest.java:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l java -o hep-rest.java -c config.json 

hep-rest.php:
	@swagger-codegen generate -i $(OPENAPI_YAML) -l php -o hep-rest.php -c config.json
