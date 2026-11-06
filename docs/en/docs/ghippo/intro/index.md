---
hide:
  - toc
MTPE: windsonsea
date: 2026-11-06
---

# What is Global Management

Global Management (Ghippo) is a comprehensive, user-centric service module that brings access control, workspaces and folders, audit logs, and platform settings together in one place. Flat management of users and groups combined with hierarchical tenant (workspace) collaboration enables platform-level access control and resource-based permission division. It also supports customizing the login page and top navigation bar, with security policies such as password rules and session timeout pre-configured, so administrators can complete basic platform settings and user management under one menu, ready to use out of the box.

![Global Management Architecture](../images/ghippo-arch.svg)

## Core Capabilities

<div class="grid cards" markdown>

- :material-shield-account-outline:{ .lg .middle } __Access Control__

    ---

    Create and manage users, groups, and roles with flexible permissions. Supports identity providers such as OIDC, LDAP, and OAuth2.

    [:arrow_forward: Access Control](../user-guide/access-control/iam.md)

- :material-view-grid-outline:{ .lg .middle } __Workspaces and Folders__

    ---

    Resource isolation units with hierarchical structure and access permission control. Organize folders by enterprise environment or department structure and control who can access which resources.

    [:arrow_forward: Workspaces and Folders](../user-guide/workspace/ws-folder.md)

- :material-text-search:{ .lg .middle } __Audit Logs__

    ---

    Record resource operations across the platform and modules for security analysis, change tracking, and troubleshooting. Audit logs can be exported.

    [:arrow_forward: Audit Logs](../user-guide/audit/audit-log.md)

- :material-cog-outline:{ .lg .middle } __Platform Settings__

    ---

    Configure security policies, mail server, appearance customization, and genuine license to keep user information secure and the platform personalized.

    [:arrow_forward: Platform Settings](../user-guide/platform-setting/mail-server.md)

- :material-chart-box-outline:{ .lg .middle } __Reports and Billing__

    ---

    Aggregate usage reports of clusters and modules, with billing management, report recalculation, and GPU usage statistics.

    [:arrow_forward: Usage Report](../user-guide/report-billing/report.md)

- :material-lock-outline:{ .lg .middle } __Personal Center__

    ---

    Manage personal account security settings such as two-factor authentication, access tokens, SSH keys, and language preference.

    [:arrow_forward: Personal Center](../user-guide/personal-center/security-setting.md)

</div>

## Procedure

Global Management is usually initialized in the following five steps for users, tenants, and basic platform policies:

```mermaid
flowchart LR
    A["① Log in to Platform<br/>Admin Privileges"] --> B["② Access Control<br/>Users · Groups · IdP"]
    B --> C["③ Workspaces and Folders<br/>Folders · Workspaces"]
    C --> D["④ Audit Logs<br/>View · Export"]
    D --> E["⑤ Platform Settings<br/>Security · Mail · Appearance"]

    click A href "../install/login/"
    click B href "../user-guide/access-control/user/"
    click C href "../user-guide/workspace/ws-folder/"
    click D href "../user-guide/audit/audit-log/"
    click E href "../user-guide/platform-setting/security/"
```

| Step | Description |
| ---- | ----------- |
| ① [Log in to the platform](../install/login.md) | Log in to the platform as the platform administrator (Admin) or a user with admin privileges |
| ② [Access Control](../user-guide/access-control/user.md) | [Create users and authorize](../user-guide/access-control/user.md), [create groups and authorize](../user-guide/access-control/group.md), and [create an identity provider](../user-guide/access-control/idprovider.md) |
| ③ [Workspaces and Folders](../user-guide/workspace/ws-folder.md) | [Create folders](../user-guide/workspace/ws-folder.md) (enterprise hierarchy) and [create workspaces](../user-guide/workspace/workspace.md) (tenants) |
| ④ [Audit Logs](../user-guide/audit/audit-log.md) | View and [export audit logs](../user-guide/audit/audit-log.md) |
| ⑤ [Platform Settings](../user-guide/platform-setting/security.md) | Configure security policy, mail server, appearance, and genuine license |

## Quick Start

<style>
.ghippo-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.ghippo-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.ghippo-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.ghippo-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.ghippo-path-step:last-child::after{display:none}
.ghippo-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.ghippo-path-title{font-weight:700;font-size:0.95rem}
.ghippo-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.ghippo-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.ghippo-path-step::after{display:none}}
</style>

<div class="ghippo-path">
  <a class="ghippo-path-step" style="--path-c:#2196f3" href="../user-guide/access-control/user/">
    <span class="ghippo-path-num">1</span>
    <span class="ghippo-path-title">Create Users and Authorize</span>
    <span class="ghippo-path-desc">Users · Groups · Roles</span>
    <span class="ghippo-path-go">Go →</span>
  </a>
  <a class="ghippo-path-step" style="--path-c:#00acc1" href="../user-guide/workspace/ws-folder/">
    <span class="ghippo-path-num">2</span>
    <span class="ghippo-path-title">Create Folders and Workspaces</span>
    <span class="ghippo-path-desc">Enterprise hierarchy · Tenant isolation</span>
    <span class="ghippo-path-go">Go →</span>
  </a>
  <a class="ghippo-path-step" style="--path-c:#43a047" href="../user-guide/workspace/wsbind-permission/">
    <span class="ghippo-path-num">3</span>
    <span class="ghippo-path-title">Bind Resources and Authorize</span>
    <span class="ghippo-path-desc">Workspace binding · Permission division</span>
    <span class="ghippo-path-go">Go →</span>
  </a>
  <a class="ghippo-path-step" style="--path-c:#fb8c00" href="../user-guide/audit/audit-log/">
    <span class="ghippo-path-num">4</span>
    <span class="ghippo-path-title">View Audit Logs</span>
    <span class="ghippo-path-desc">Operation records · Security analysis</span>
    <span class="ghippo-path-go">Go →</span>
  </a>
</div>

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Feature List__

    ---

    View the complete feature list of Global Management covering access control, workspaces and folders, audit logs, and platform settings.

    [:arrow_forward: View the feature list](features.md)

- :material-book-open-page-variant:{ .lg .middle } __Glossary__

    ---

    Learn common terms and concepts in Global Management, such as IAM, folder, workspace, and resource binding.

    [:arrow_forward: View the glossary](glossary.md)

- :material-chat-question-outline:{ .lg .middle } __FAQs__

    ---

    Common issues and troubleshooting for installation, login, and usage of Global Management.

    [:arrow_forward: View FAQs](faq.md)

- :material-map-outline:{ .lg .middle } __Best Practices__

    ---

    Practical recommendations for workspace planning, permission assignment, folder design, and OEM customization.

    [:arrow_forward: View best practices](../best-practice/ws-best-practice.md)

</div>

[Start Free Trial Now](../../dce/license0.md){ .md-button .md-button--primary }
[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
[Read the Global Management User Guide (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/ghippo.pdf){ .md-button .md-button--primary }
