# End-to-end Traffic lane

The microservice engine supports isolating relevant versions of an application (or other features) into an independent runtime environment (i.e., a lane), and then routing traffic that meets the rules of the lane to the target version (or other feature) of the application by setting lane rules.
This article introduces the concept of traffic lanes and their use cases.

## Features

Gray release will forward a small part of online traffic to the new version of the service based on the request content or the proportion of request traffic. After the gray verification is passed, gradually increase the request traffic of the new version, which is a progressive release method.

When there are call chains between services, gray release of services often extends beyond individual services and requires environment isolation and traffic control for the entire request chain of services,
ensuring that gray traffic only goes to the gray version of services in the call chain, achieving isolation between call chains.

A lane is an isolation environment composed of different services with the same version (or other features).
By using the traffic lane feature, you only need to specify a small number of governance rules to build multiple traffic isolation environments from the gateway to the entire backend services,
effectively ensuring the smooth and secure release of multiple services and the parallel development of multiple versions of services, further promoting the rapid development of the business.
