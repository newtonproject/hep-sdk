all:hep-sdk.py hep-sdk.java hep-sdk.php
	@echo "Generate success"

hep-sdk.py:
	@swagger-codegen generate -i swagger.yaml -l python -o hep-sdk.py

hep-sdk.java:
	@swagger-codegen generate -i swagger.yaml -l java -o hep-sdk.java

hep-sdk.php:
	@swagger-codegen generate -i swagger.yaml -l php -o hep-sdk.php
