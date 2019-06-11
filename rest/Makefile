all:hep_rest.py hep_rest.java hep_rest.php
	@echo "Generate success"

hep_rest.py:
	@swagger-codegen generate -i swagger.yaml -l python -o hep_rest.py -c config.json

hep_rest.java:
	@swagger-codegen generate -i swagger.yaml -l java -o hep_rest.java -c config.json 

hep_rest.php:
	@swagger-codegen generate -i swagger.yaml -l php -o hep_rest.php -c config.json
