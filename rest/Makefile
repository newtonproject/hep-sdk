all:hep.py hep.java hep.swift
	@echo "Generate success"

hep.py:
	@swagger-codegen generate -i swagger.yaml -l python -o hep.py

hep.java:
	@swagger-codegen generate -i swagger.yaml -l java -o hep.java

hep.swift:
	@swagger-codegen generate -i swagger.yaml -l swift4 -o hep.swift
