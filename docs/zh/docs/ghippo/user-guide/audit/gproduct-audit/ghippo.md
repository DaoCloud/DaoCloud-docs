# 全局管理审计项汇总

|   事件名称  |  资源类型   |   备注  |
| --- | --- | --- |
| 修改用户email：UpdateEmail-Account | Account |     |
| 修改用户密码：UpdatePassword-Account | Account |     |
| 创建sk：CreateAccessKeys-Account | Account |     |
| 修改sk：UpdateAccessKeys-Account | Account |     |
| 删除sk：DeleteAccessKeys-Account | Account |     |
| 创建用户：Create-User | User |     |
| 删除用户：Delete-User | User |     |
| 更新用户信息：Update-User | User |     |
| 更新用户角色： UpdateRoles-User | User |     |
| 设置用户密码： UpdatePassword-User | User |     |
| 创建用户密钥： CreateAccessKeys-User | User |     |
| 更新用户密钥： UpdateAccessKeys-User | User |     |
| 删除用户密钥：DeleteAccessKeys-User | User |     |
| 创建用户组：Create-Group | Group |     |
| 删除用户组：Delete-Group | Group |     |
| 更新用户组：Update-Group | Group |     |
| 添加用户至用户组：AddUserTo-Group | Group |  |
| 从用户组删除用户： RemoveUserFrom-Group | Group |     |
| 更新用户组角色： UpdateRoles-Group | Group |     |
| 角色关联用户：UpdateRoles-User | User |     |
| 创建Ldap ：Create-LADP | LADP |     |
| 更新Ldap：Update-LADP | LADP |     |
| 删除Ldap ： Delete-LADP | LADP | OIDC没有走APIserver审计不到 |
| 登录：Login-User | User |     |
| 登出：Logout-User | User |     |
| 设置密码策略：UpdatePassword-SecurityPolicy | SecurityPolicy |     |
| 设置会话超时：UpdateSessionTimeout-SecurityPolicy | SecurityPolicy |     |
| 设置账号锁定：UpdateAccountLockout-SecurityPolicy | SecurityPolicy |     |
| 设置自动登出：UpdateLogout-SecurityPolicy | SecurityPolicy |     |
| 邮件服务器设置 MailServer-SecurityPolicy | SecurityPolicy |     |
| 外观定制 CustomAppearance-SecurityPolicy | SecurityPolicy |     |
| 正版授权 OfficialAuthz-SecurityPolicy | SecurityPolicy |     |
| 创建工作空间：Create-Workspace | Workspace |     |
| 删除工作空间：Delete-Workspace | Workspace |     |
| 绑定资源：BindResourceTo-Workspace | Workspace |     |
| 解绑资源：UnBindResource-Workspace | Workspace |     |
| 绑定共享资源：BindShared-Workspace | Workspace |     |
| 设置资源配额：SetQuota-Workspace | Workspace |     |
| 工作空间授权：Authorize-Workspace | Workspace |     |
| 删除授权 DeAuthorize-Workspace | Workspace |     |
| 编辑授权 UpdateDeAuthorize-Workspace | Workspace |     |
| 更新工作空间 Update-Workspace | Workspace |     |
| 创建文件夹：Create-Folder | Folder |     |
| 删除文件夹：Delete-Folder | Folder |     |
| 编辑文件夹授权：UpdateAuthorize-Folder | Folder |     |
| 更新文件夹：Update-Folder | Folder |     |
| 新增文件夹授权：Authorize-Folder | Folder |     |
| 删除文件夹授权：DeAuthorize-Folder | Folder |     |
| 设置审计日志自动清理：AutoCleanup-Audit | Audit |     |
| 手动清理审计日志：ManualCleanup-Audit | Audit |     |
| 导出审计日志：Export-Audit | Audit |     |