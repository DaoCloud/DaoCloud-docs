# Push image

After creating managed Harbor and registry space, you can follow the instructions below to log in and push the image to the container registry; or log in to native Harbor to view the guidance provided by native Harbor under each registry space (project).

## Push method one

Prerequisite: Managed Harbor and registry space have been created

You can build a new container image locally or grab a public image from DockerHub for testing. This page takes the latest official Nginx image of DockerHub as an example. Execute the following commands in sequence in the command line tool to push the image. Please replace library and `nginx` with the name of the registry space and container registry you actually created.

1. Log in to the container registry

    ```bash
    docker login --username=<container registry login name> <container registry address>
    ```

    Example: `docker login --username=admin http://test.lrf02.kangaroo.com`

    Enter the container registry password in the returned result (the password set when creating managed Harbor)

1. Push image

    Execute the following command to label the image

    ```bash
    docker tag <container registry name>:<artifact version> <container registry address>/<registry space name>/<container registry name>:<artifact version>
    ```

    Example: `docker tag nginx:latest http://test.lrf02.kangaroo.com/library/nginx:latest`

    Execute the following command to push the image to the registry space library

    ```bash
    docker push <container registry address>/<registry space name>/<container registry name>:<artifact version>
    ```

    Example: `docker push http://test.lrf02.kangaroo.com/library/nginx:latest`

1. Pull the image

    Execute the following command to pull the image.

    ```bash
    docker pull <container registry address>/<registry space name>/<container registry name>:<artifact version>
    ```

    Example: `docker pull http://test.lrf02.kangaroo.com/library/nginx:latest`

## Push method 2

Prerequisite: Managed Harbor and registry space have been created

1. On the Managed Harbor list page, click `...` on the right side of the target registry, click `Native Harbor` to enter the login page of the native Harbor.

    

1. Enter the user name and password set when creating managed Harbor to enter native Harbor

    

1. Click the name of the target registry space (project) to enter the registry space

    

1. Click the push command on the right to view the push commands provided by native Harbor.

    

!!! tip

    Compared with method 1, the push command of the native Harbor automatically fills in the address of the container registry and the name of the registry space.
