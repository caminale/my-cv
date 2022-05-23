.PHONY: push
push:
	./bin/autocommit


.PHONY: website_publish
website_publish:
	./bin/web_publish.py
