---
title: '绑定代码源后，是否会存在安全隐患 ?'
markdown:
    extra: true
gravui:
    enabled: true
    tabs: true
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!-- 

介绍 OAuth 和 Deploy Key 的后台实现，强调我们对代码库的操作是规范安全的。

OAuth登陆安全，无密码保存
Deploy Key，对代码进行访问，删除后无法访问（主动撤销权限的办法）
CI／Build过程中，对 code 的保留，实质性删除
密保登陆安全

-->