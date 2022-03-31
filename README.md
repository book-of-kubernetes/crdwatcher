## CRD Watcher Container Image

This repository contains a simple Python script that watches for changes
in cluster objects defined by a CustomResourceDefinition (CRD). It is 
intended to illustrate how a CRD can be used to extend the behavior of a
Kubernetes cluster.

This image is published to Docker Hub, so you can use it without having to
build it. It is designed to run in a Kubernetes cluster where it can access
the API server. See the book for details.

You are welcome to rebuild this image and publish it to your own container
registry. To build it with Docker, run:

```
docker build -t <tag> .
```
