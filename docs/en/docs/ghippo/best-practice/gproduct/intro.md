---
hide:
  - toc
---

# How GProduct connects to global management

GProduct is the general term for all other modules in DCE except the global management. These modules need to be connected with the global management before they can be added to DCE.

## What to be docking

- [Docking Navigation Bar](./nav.md)

    The entrances are unified on the left navigation bar.

- [Access Routing and AuthN](route-auth.md)

    Unify the IP or domain name, and unify the routing entry through the globally managed Istio Gateway.

- Unified login / unified AuthN authentication

    The login page is unified using the global management (Keycloak) login page, and the API authn token verification uses Istio Gateway.
    After GProduct is connected to the global management, there is no need to pay attention to how to implement login and authentication.

## Video Demonstrations and PDF

For integrating DCE into a customer system (OEM OUT), see the [OEM OUT documentation](../oem/oem-out.md).

<div class="responsive-video-container">
<video controls src="https://harbor-test2.cn-sh2.ufileos.com/docs/videos/oem-out.mp4" preload="metadata" poster="../../../videos/images/oem-out.png"></video>
</div>

For integrating a customer system into DCE (OEM IN), see the [OEM IN documentation](../oem/oem-in.md).

<div class="responsive-video-container">
<video controls src="https://harbor-test2.cn-sh2.ufileos.com/docs/videos/oemin-istio.mp4" preload="metadata" poster="../../../videos/images/oem-in.png"></video>
</div>
