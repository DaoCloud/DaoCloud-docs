---
hide:
  - toc
---

# End Device Overview

An end device is the layer closest to the physical world in the device-edge-cloud architecture of Cloud Edge Collaboration. It can range from sensors and controllers to smart cameras or industrial computers. End devices connect to edge nodes over protocols such as Modbus and are then managed centrally from the cloud. The platform uses a **device model** to describe the information a device exposes and a **device twin** to record its live state; together they form the cloud-side digital view of the device.

## Key Concepts

| Concept | Description |
| --- | --- |
| **End Device** | A physical device connected to an edge node, accessible over protocols such as Modbus. Once connected, it can be managed centrally from the cloud, including its basic information, twin attributes, labels, and access settings. See [Create End Device](./create-device.md). |
| **Device Model** | A digital representation of an end device in the cloud. It abstracts the common characteristics of a device type into a data model, using attributes to define the device and the information it can provide externally. See [Create Device Model](./create-device-model.md). |
| **Device Twin** | The dynamic data of an end device (twin attributes). It records both the **desired value** set by applications and the **actual value** reported by the device, such as the on/off status of a light. See [Manage End Device](./manage-device.md). |

## How Device Twin Works

A device twin has the same characteristics as the physical device and acts as the intermediary between the device and applications: commands sent by an application first reach the device twin and update its desired state, while the device reports its actual state in real time; the twin records both values.

![Device twin](../../images/device-twin.svg)

| Action | Direction | Effect |
| --- | --- | --- |
| **Data Reporting** | End device → Edge node (actual state) | The device writes its live state into the actual value of the device twin for applications on the edge node to read. |
| **Device Control** | Edge node (desired state) → End device | An application changes the desired value of the device twin, which the edge node sends down to the device to change its state. |
| **State Synchronization** | Device offline → Back online | When the device comes back online, it resynchronizes from the state kept in the device twin without being reconfigured. |

In the Cloud Edge Collaboration module, an end device can be created and associated with an edge node. Once associated, the twin attribute information of the device is stored on the edge node. Applications running on the edge node can read the actual values of the twin attributes and modify the desired values to change the device's state.

## Workflow

The typical steps for managing and controlling end devices are as follows:

<style>
.dev-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.dev-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.dev-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.dev-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.dev-path-step:last-child::after{display:none}
.dev-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.dev-path-title{font-weight:700;font-size:0.95rem}
.dev-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.dev-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.dev-path-step{flex:1 1 calc(50% - 0.75rem)}.dev-path-step::after{display:none}}
</style>

<div class="dev-path">
  <a class="dev-path-step" style="--path-c:#2196f3" href="create-device-model/">
    <span class="dev-path-num">1</span>
    <span class="dev-path-title">Create Device Model</span>
    <span class="dev-path-desc">Abstract the common characteristics of a device type and use attributes to define the data the device provides.</span>
    <span class="dev-path-go">Go →</span>
  </a>
  <a class="dev-path-step" style="--path-c:#00acc1" href="create-device/">
    <span class="dev-path-num">2</span>
    <span class="dev-path-title">Create End Device</span>
    <span class="dev-path-desc">Create a device instance in an edge unit and fill in its basic information and access settings.</span>
    <span class="dev-path-go">Go →</span>
  </a>
  <a class="dev-path-step" style="--path-c:#43a047" href="create-device/">
    <span class="dev-path-num">3</span>
    <span class="dev-path-title">Associate with an Edge Node</span>
    <span class="dev-path-desc">Select "Bind Node" in the device list. The edge node then stores the device's twin attributes, and the device starts reporting state and receiving commands.</span>
    <span class="dev-path-go">Go →</span>
  </a>
  <a class="dev-path-step" style="--path-c:#fb8c00" href="manage-device/">
    <span class="dev-path-num">4</span>
    <span class="dev-path-title">Manage and Monitor</span>
    <span class="dev-path-desc">Edit basic information, twin attributes, labels, and access settings, and monitor device status.</span>
    <span class="dev-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
