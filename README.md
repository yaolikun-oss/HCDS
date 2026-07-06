# HCDS（History Character Dataset Standard）

Version：v2.0 RC1

---

# What is HCDS

History Character Dataset Standard（HCDS）

是一套面向历史人物 AI 生产线的数据标准。

HCDS 不是：

- LoRA 项目
- Prompt 项目
- ComfyUI 项目

而是整个 AI 生产线的数据底座（Data Foundation）。

---

# Project Vision

建立业内最高标准的历史人物数据标准。

实现：

Character Profile

↓

Dataset Generator

↓

Prompt Generator

↓

ComfyUI

↓

Caption

↓

Metadata

↓

OneTrainer

↓

LoRA

↓

Flux

↓

Wan

↓

Video

全部自动生成。

---

# Design Philosophy

HCDS 不维护 Prompt。

HCDS 不维护 Caption。

HCDS 不维护 Dataset。

HCDS 只维护：

Character

Attribute

Rule

其它所有内容全部自动生成。

---

# Single Source of Truth

整个项目只有一个唯一数据源：

HCDS_Master.xlsx

任何信息，

只能维护一份。

包括：

Character

Prompt

Caption

Metadata

Image Name

OneTrainer Dataset

全部由 HCDS_Master 自动生成。

禁止人工维护多个版本。

---

# Core Principles

## Principle 1

人物（Character）

与

场景（Scene）

彻底解耦。

LoRA：

学习人物。

Flux：

学习背景。

Wan：

学习视频。

---

## Principle 2

动作（Action）

与

情绪（Emotion）

彻底解耦。

图片：

学习动作。

Caption：

保留情绪。

建立：

Emotion Mapping。

---

## Principle 3

任何抽象描述，

必须转换成：

可观察动作。

例如：

×

威严站立

×

自然站立

×

霸气站立

统一改为：

√

双手背后

√

扶剑

√

双手自然下垂

√

双手交握腹前

---

## Principle 4

Excel

永远是：

Single Source of Truth。

Claude

Codex

Python

ComfyUI

OneTrainer

全部读取Excel。

禁止任何程序维护自己的Prompt。

---

# HCDS Architecture

Character Library

↓

Attribute Library

↓

Rule Engine

↓

Dataset Generator

↓

Prompt Generator

↓

ComfyUI

↓

Image

↓

Caption

↓

Metadata

↓

OneTrainer

↓

LoRA

↓

Flux

↓

Wan

↓

Video

---

# Module Structure

HCDS

├── Character

├── Attribute

├── Rule

├── Dataset

├── Prompt

├── Caption

├── Metadata

├── Training

└── Automation

---

# AI Responsibilities

Claude

负责：

Dataset Generation

Prompt Generation

Automation

Codex

负责：

Python

Generator

Automation

Testing

ChatGPT

负责：

Architecture

Schema

Design Decisions

Documentation

---

# Development Rule

任何新增功能，

必须满足：

1.

机器可读

Machine Readable

2.

自动生成

Auto Generated

3.

可扩展

Extensible

4.

唯一数据源

Single Source of Truth

否则：

不得进入HCDS。

---

# Future

HCDS未来不仅服务：

OneTrainer

还将服务：

Flux

Wan

Qwen Image Edit

LTX

Cosmos

OpenAI Video

所有历史人物AI工作流共享同一数据标准。
