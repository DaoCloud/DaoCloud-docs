---
hide:
  - toc
---

# How GProduct connects to global management

GProduct is the general term for all other modules in DCE 5.0 except the global management. These modules need to be connected with the global management before they can be added to DCE 5.0.

## What to be docking

- [Docking Navigation Bar](./nav.md)

    The entrances are unified on the left navigation bar.

- [Access Routing and AuthN](route-auth.md)

    Unify the IP or domain name, and unify the routing entry through the globally managed Istio Gateway.

- Unified login / unified AuthN authentication

    The login page is unified using the global management (Keycloak) login page, and the API authn token verification uses Istio Gateway.
    After GProduct is connected to the global management, there is no need to pay attention to how to implement login and authentication.
