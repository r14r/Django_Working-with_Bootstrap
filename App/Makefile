PREFIX_PKG := django_tutorial_app

VERSION_BOOTSTRAP := 4.4.1
default:
	grep -E ':\s+#' Makefile

clearcache:	# Clear Cache
	python3 manage.py clearcache

run:		# Run Server
	python3 manage.py runserver 8000

deploy:		# Deploy
	rm -rf dist $(PREFIX_PKG)*
	rm -rf app.dist
	cd app && python3 setup.py sdist
	mkdir app.dist && mv app/dist/* app/$(PREFIX_PKG)* app.dist

bootstrap_install:	# Install Bootstrap Library
	cd .. && yarn add bootstrap
	rm -rf  app/static/bootstrap
	mkdir   app/static/bootstrap
	cp -R ../node_modules/bootstrap/dist/* app/static/bootstrap

query_install:		# Install jQuery Library
	cd .. && yarn add jquery
	rm -rf app/static/jquery
	mkdir  app/static/jquery
	cp ../node_modules/jquery/dist/* app/static/jquery

bootstrap_download:	# Install Bootstrap from Source
	# https://github.com/twbs/bootstrap/archive/v4.4.1.zip
	mkdir -p install/bootstrap
	wget  -q https://github.com/twbs/bootstrap/archive/v$(VERSION_BOOTSTRAP).zip                                               -O install/bootstrap/$(VERSION_BOOTSTRAP).zip
	wget  -q https://github.com/twbs/bootstrap/releases/download/v$(VERSION_BOOTSTRAP)/bootstrap-$(VERSION_BOOTSTRAP)-dist.zip -O install/bootstrap/$(VERSION_BOOTSTRAP)-dist.zip

bootstrap_unpack:
	rm -rf   app/static/vendor/bootstrap/bootstrap-$(VERSION_BOOTSTRAP)-dist
	unzip -q install/bootstrap/$(VERSION_BOOTSTRAP)-dist.zip -d       app/static/vendor/bootstrap/
	#
	rm -rf   app/static/vendor/bootstrap/$(VERSION_BOOTSTRAP)
	mv       app/static/vendor/bootstrap/bootstrap-$(VERSION_BOOTSTRAP)-dist app/static/vendor/bootstrap/$(VERSION_BOOTSTRAP)
