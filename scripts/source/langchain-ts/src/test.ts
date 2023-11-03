const replacedImagePath =  '# 创建虚拟机\n' +
'\n' +
'本文将介绍如何通过镜像和 YAML 文件两种方式创建虚拟机。\n' +
'\n' +
'虚拟机容器基于 KubeVirt 技术将虚拟机作为云原生应用进行管理，与容器无缝地衔接在一起，\n' +
'使用户能够轻松地部署虚拟机应用，享受与容器应用一致的丝滑体验。\n' +
'\n' +
'## 前提条件\n' +
'\n' +
'创建虚拟机之前，需要满足以下前提条件：\n' +
'\n' +
'- 在集群内安装 virtnest-agent。\n' +
'- 创建一个[命名空间](../../kpanda/user-guide/namespaces/createns.md)和[用户](../../ghippo/user-guide/access-control/user.md)。\n' +
'- 当前操作用户应具有\n' +
'  [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)\n' +
'  或更高权限，详情可参考[命名空间授权](../../kpanda/user-guide/namespaces/createns.md)。\n' +
'- 提前准备好镜像。';

const path = "../../kpanda/user-guide/namespaces/createns.md";

function replacePath(path) {
  const pattern = /\.\.\/\.\.\/(.+?)\.md/g;
  const replacedPath = path.replace(pattern, "https://docs.daocloud.io/$1");
  return replacedPath;
}

const replacedPath = replacePath(replacedImagePath);
console.log(replacedPath);
