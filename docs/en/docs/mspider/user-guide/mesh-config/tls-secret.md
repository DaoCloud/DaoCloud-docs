# TLS key management

Secret is an object stored in the form of key/value pairs, containing sensitive information such as certificates, private keys, and credentials, and is used for link TLS encrypted communication between services.
The service mesh provides an interface for TLS key management.

## Prepare credentials and private key

For this example, use a self-signed CA to issue a test certificate for helloworld. Create the output directory and CA certificate and private key first, then generate and sign the helloworld certificate signing request (CSR).

```shell
mkdir -p example_certs1
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj "/CN=example.com/O=example organization" -keyout example_certs1/example.com.key -out example_certs1/example.com.crt
openssl req -out example_certs1/helloworld.example.com.csr -newkey rsa:2048 -nodes -keyout example_certs1/helloworld.example.com.key -subj "/CN=helloworld.example.com/O=helloworld organization"
openssl x509 -req -sha256 -days 365 -CA example_certs1/example.com.crt -CAkey example_certs1/example.com.key -set_serial 1 -in example_certs1/helloworld.example.com.csr -out example_certs1/helloworld.example.com.crt
```

Display the generated certificate and private key, and copy their complete PEM contents (including the `BEGIN` and `END` lines) into the TLS key form below.
Use the `.crt` certificate, not the `.csr` certificate signing request.

```shell
cat example_certs1/helloworld.example.com.crt
cat example_certs1/helloworld.example.com.key
```

## Create key

1. After entering a mesh, click __Mesh Configuration__ -> __TLS Key Management__ in the left navigation bar, and click the __Create__ button.

     

1. Fill in the name, select the namespace, fill in the newly created certificate and private key, add labels according to the situation, and click __OK__ .

     

1. The screen prompts that the creation is successful. Click the __┇__ button on the right to perform operations such as editing, YAML editing, and deletion.

     

To view the Secret YAML for the same certificate and private key, run the following command. `--dry-run=client` generates YAML without creating a resource in the cluster:

```shell
kubectl create secret tls secret001 \
  --cert=example_certs1/helloworld.example.com.crt \
  --key=example_certs1/helloworld.example.com.key \
  --dry-run=client -o yaml
```

## Use Cases

Created TLS keys can be used to:

1. __Destination Rules__ . When adding policy configuration, after enabling client TLS, you can choose the created key in the following two modes:

     - Simple mode
     - Bidirectional mode

     

1. __Gateways__ . After enabling the server-side TLS mode, you can choose the created key in the following 3 modes:

     - Simple mode
     - Bidirectional mode
     - Istio bidirectional mode

     
