# Release Notes

> 记录文档站版本更新记录，后续更新请在顶部更新

---

## 文档站 Release v1.0

经过一段时间的打磨，随着广大爱好者的贡献，文档站趋于成熟；为了帮助大家更高效的维护文档站，此次发布 v1.0 集合了最近诸多能力升级。

### 新版目录结构

```bash
docs
├── README.md
├── en                    # 英文
│   ├── docs              # 原 `docs/en`
│   ├── mkdocs.yml        # Mkdocs 配置文件
│   ├── navigation.yml    # 文件导航
│   └── theme
└── zh                    # 中文
    ├── docs              # 原 `docs/zh`
    ├── mkdocs.yml        # Mkdocs 配置文件
    ├── navigation.yml    # 文件导航
    └── theme
```

### 升级

- 优化: 更标准化的多语言文档站架构
- 优化: 剔除英文文档重复编译带来编译耗时，缩减大量静态文档编译耗时
- 优化: 拆分文档站配置文件与目录导航
- Fix: 中文/英文 搜索互相干扰问题
