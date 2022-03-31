#!/usr/bin/env python3
from kubernetes import client, config, watch
import json, os, sys

config.load_kube_config()
group = os.environ.get('WATCH_GROUP', 'bookofkubernetes.com')
version = os.environ.get('WATCH_VERSION', 'v1')
namespace = os.environ.get('WATCH_NAMESPACE', 'default')
resource = os.environ.get('WATCH_RESOURCE', 'samples')

api = client.CustomObjectsApi()

w = watch.Watch()
for event in w.stream(api.list_namespaced_custom_object,
        group=group, version=version, namespace=namespace, plural=resource):
  json.dump(event, sys.stdout, indent=2)
