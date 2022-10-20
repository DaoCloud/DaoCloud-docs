# support mkdocs-material-insider
IMAGE_HUB ?= release.daocloud.io/
BASE_IMAGE ?= ${IMAGE_HUB}daocloud/ndx-mkdocs-material
BASE_IMAGE_VERSION ?= v1.1.1

INS_IMAGE_HUB ?= release-ci.daocloud.io/
INS_IMAGE ?= ${INS_IMAGE_HUB}product/ndx-mkdocs-material-insider
INS_IMAGE_VERSION ?= v1.1.1

help:
	@echo
	@echo "使用:"
	@echo '    make [指令]'
	@echo
	@echo "指令:"
	@echo '    serve                使用 docker 启动服务，默认端口8000'
	@echo '    in-serve             内部使用，使用 docker 启动服务，默认端口8000'
	@echo '    clean                清理静态文件'
	@echo '    help                 显示帮助信息'
	@echo
	@echo "版本: DaoCloud-docs 1.0.0 20220921"
	@echo

serve:
	docker run --rm -it -e ENABLED_GIT_REVISION_DATE="false" -p 8000:8000 -v ${PWD}/docs/zh:/docs ${BASE_IMAGE}:${BASE_IMAGE_VERSION}

in-serve:
	docker run --rm -it -e ENABLED_GIT_REVISION_DATE="false" -p 8000:8000 -v ${PWD}:/docs ${INS_IMAGE}:${INS_IMAGE_VERSION}

clean:
	rm -rf public site


.PHONY: clean serve in-serve help
