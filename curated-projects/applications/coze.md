# Coze / 扣子

## 基本信息
- **官网**: https://coze.cn (国内版) / https://coze.com (国际版)
- **类型**: 一站式 AI Bot 开发平台
- **维护者**: 字节跳动 (ByteDance)

## 简介

Coze（扣子）是字节跳动推出的 AI Bot 开发平台，提供一站式的 AI 应用开发、部署和管理服务。用户无需编程经验即可快速创建各种 AI Bot，并发布到多个平台。

## 核心特点

### 无代码开发
- **可视化编排** - 通过拖拽构建工作流
- **丰富节点** - 支持多种功能节点
- **即时预览** - 实时测试和调试

### 知识库
- **多格式支持** - 支持文档、网页、API 等
- **智能检索** - 语义搜索能力
- **灵活配置** - 可定制检索策略

### 多平台发布
- **飞书** - 集成飞书消息
- **微信** - 微信公众号/小程序
- **Discord** - Discord 机器人
- **Telegram** - Telegram 机器人
- **自定义 API** - 开放 API 接口

### 插件系统
- **官方插件** - 丰富的内置插件
- **自定义插件** - 支持扩展功能
- **API 集成** - 连接外部服务

## 适用场景

- 客服机器人
- 私人助理
- 内容创作助手
- 数据分析 Bot
- 教育辅导 Bot
- 企业内部助手

## 快速开始

### 在线使用
1. 访问 https://coze.cn
2. 注册并登录
3. 点击"创建 Bot"
4. 配置名称、描述和图标
5. 使用可视化编辑器编排工作流
6. 添加知识库（可选）
7. 发布到目标平台

### API 调用
```bash
curl -X POST https://api.coze.cn/v1/chat \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "bot_id": "your-bot-id",
    "user_id": "user123",
    "query": "你好",
    "stream": false
  }'
```

## 学习资源

- [官方文档](https://coze.cn/docs)
- [B站教程](https://search.bilibili.com/all?keyword=coze%E6%89%81%E5%AD%90)
- [GitHub (Bot Framework)](https://github.com/coze-dev)

## 推荐理由

Coze 是国内最流行的 AI Bot 开发平台之一。它的无代码编辑器让任何人都能创建强大的 AI 应用。丰富的插件和发布渠道使其成为企业快速落地 AI 应用的绝佳选择。
