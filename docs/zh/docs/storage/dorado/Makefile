SHELL := /bin/bash
FILTER := -l task=pvc-test --wait=false --ignore-not-found=true

.EXPORT_ALL_VARIABLES:
DOCKER_BUILDKIT := 1

csi:
	helm upgrade --install esdk ./helm/esdk \
		-n huawei-csi --create-namespace
csm:
	helm upgrade --install csm ./helm/huawei-csm \
		-n huawei-csm --create-namespace \
		--set features.prometheusCollector.prometheusCollectorSSL.enabled=false \
		--set cluster.name=dce5

csm-log:
	kubectl -n huawei-csm exec -it deploy/csm-storage-service -c cmi-controller \
		-- cat /var/log/huawei-csm/csm-storage-service/cmi-service

backend:
	oceanctl delete backend dorado-nas || true
	oceanctl create backend -i yaml -f backends.yaml
b: backend

backend_admin:
	oceanctl delete backend dorado-nas || true
	oceanctl create backend -i yaml -f backends_admin.yaml
ba: backend_admin

create:
	kubectl apply -f sc.yaml

	kubectl apply -f pvc.yaml
	kubectl wait pvc/data-mysql \
		--for=jsonpath='{.status.phase}'='Bound' \
		--timeout=600s

	kubectl apply -f mysql.yaml
	kubectl rollout status --watch --timeout=600s sts/mysql

	kubectl apply -f pvc-expand.yaml
	kubectl wait pvc/data-mysql \
		--for=jsonpath='{.status.capacity.storage}'='2Gi' \
		--timeout=600s

	kubectl apply -f pvc-clone.yaml
	kubectl wait pvc/data-mysql-clone \
		--for=jsonpath='{.status.phase}'='Bound' \
		--timeout=600s
	kubectl apply -f mysql-clone.yaml
	kubectl rollout status --watch --timeout=600s sts/mysql-clone

	kubectl apply -f snapshotclass.yaml
	kubectl apply -f snapshot.yaml
	kubectl wait volumesnapshot/data-mysql-snapshot \
		--for=jsonpath='{.status.readyToUse}'=true \
		--timeout=600s
	kubectl apply -f mysql-restore.yaml
	kubectl rollout status --watch --timeout=600s sts/mysql-restore
c: create

delete:
	kubectl delete svc $(FILTER)
	kubectl delete sts $(FILTER)
	kubectl delete volumesnapshot $(FILTER)
	kubectl delete vsclass $(FILTER)
	kubectl delete pvc $(FILTER)
	kubectl delete sc $(FILTER)
d: delete

watch:
	watch kubectl get po,pvc,volumesnapshot
w: watch

sync-doc:
	rsync -av ../../../../../../huawei-dorado-test/ . \
		--include='img' \
		--include='*.md' \
		--exclude='*' \
		--delete
sd: sync-doc
