# Dataset Plan 100 Rules

Version: v2.0 RC1  
Status: Draft  
Target Sheet: Dataset_Plan  
Purpose: 为每一个历史人物生成 100 个标准采集位

---

## 1. 核心原则

Dataset_Plan 不是最终训练数据。

它是“采集计划”。

最终训练数据由 Dataset_Plan 自动生成 Dataset_Master。

流程：

```text
Character_Profile
+ Attribute_Library
+ Rule_Engine
+ Dataset_Plan
↓
Dataset_Master
↓
Prompt / Image / Caption / Metadata / OneTrainer Dataset
```

---

## 2. 100采集位结构

每个人物默认生成 100 张标准采集图。

| Group_ID | 组名 | 数量 | Dataset_Use |
|---|---|---:|---|
| G01 | 标准身份视角 | 15 | train |
| G02 | 站姿动作 | 20 | train |
| G03 | 坐姿动作 | 15 | train |
| G04 | 行走与转身 | 10 | train |
| G05 | 手部与持物 | 15 | train |
| G06 | 表情变化 | 10 | train |
| G07 | 骑马增强 | 10 | train |
| G08 | 场景参考 | 5 | reference |

合计：100

---

## 3. Scene_Type

允许值：

```text
Character_Base
Character_Action
Character_Sitting
Character_Motion
Character_Hand
Character_Expression
Character_Horse
Character_Reference
```

---

## 4. Dataset_Use

允许值：

```text
train
reference
exclude
```

规则：

* `train`：进入 LoRA 训练。
* `reference`：作为角色参考图，不进入训练。
* `exclude`：废弃，不进入后续流程。

默认：

* G01-G07：train
* G08：reference

---

## 5. G01 标准身份视角：15张

目标：学习人物核心身份、脸、身材、服饰。

要求：

* 背景简单
* 不出现复杂建筑
* 不出现场景叙事
* 不出现朝堂、战场、大帐等环境

采集位：

| 序号 | View                   |
| -: | ---------------------- |
| 01 | front view             |
| 02 | left 45 degree         |
| 03 | right 45 degree        |
| 04 | left profile           |
| 05 | right profile          |
| 06 | back view              |
| 07 | upper body             |
| 08 | full body              |
| 09 | close-up               |
| 10 | medium shot            |
| 11 | low angle              |
| 12 | high angle             |
| 13 | three-quarter view     |
| 14 | slight head turn left  |
| 15 | slight head turn right |

Scene_Type：

```text
Character_Base
```

---

## 6. G02 站姿动作：20张

目标：用可观察动作替代抽象姿态词。

禁止使用：

```text
威严站立
自然站立
霸气站立
沉稳站立
```

统一改成可观察动作。

采集位：

| 序号 | Pose / Action                            |
| -: | ---------------------------------------- |
| 01 | hands naturally at sides                 |
| 02 | hands behind back                        |
| 03 | hands clasped in front                   |
| 04 | one hand on sword hilt                   |
| 05 | one hand on jade belt                    |
| 06 | arms crossed                             |
| 07 | traditional salute                       |
| 08 | hands inside sleeves                     |
| 09 | one hand raised slightly                 |
| 10 | standing with one foot forward           |
| 11 | standing with both feet together         |
| 12 | standing with shoulders squared          |
| 13 | standing with body slightly turned left  |
| 14 | standing with body slightly turned right |
| 15 | standing with head slightly lowered      |
| 16 | standing while looking forward           |
| 17 | standing while looking sideways          |
| 18 | standing with cloak hanging naturally    |
| 19 | standing with belt visible               |
| 20 | standing with sword at waist             |

Scene_Type：

```text
Character_Action
```

---

## 7. G03 坐姿动作：15张

目标：学习坐姿结构，不让 LoRA 学朝堂、龙椅、宫殿。

注意：

* 不强制出现椅子。
* 不强制出现朝堂。
* 不强制出现御案。
* 重点是人物坐姿、衣摆、身体结构。

采集位：

| 序号 | Posture / Action                        |
| -: | --------------------------------------- |
| 01 | sitting upright                         |
| 02 | sitting front view                      |
| 03 | sitting three-quarter view              |
| 04 | sitting with hands on knees             |
| 05 | sitting with hands clasped              |
| 06 | sitting while reading scroll            |
| 07 | sitting while holding brush             |
| 08 | sitting while looking sideways          |
| 09 | sitting while thinking                  |
| 10 | sitting with one hand on table          |
| 11 | sitting with both hands on table        |
| 12 | sitting with body slightly turned left  |
| 13 | sitting with body slightly turned right |
| 14 | sitting with serious expression         |
| 15 | sitting with calm expression            |

Scene_Type：

```text
Character_Sitting
```

---

## 8. G04 行走与转身：10张

目标：为后续视频生成准备动作基础。

采集位：

| 序号 | Motion                              |
| -: | ----------------------------------- |
| 01 | walking forward                     |
| 02 | slow walking                        |
| 03 | stepping forward                    |
| 04 | turning body                        |
| 05 | looking back                        |
| 06 | side walking                        |
| 07 | walking with hands behind back      |
| 08 | walking while holding scroll        |
| 09 | walking while holding sword         |
| 10 | cloak moving slightly while walking |

Scene_Type：

```text
Character_Motion
```

---

## 9. G05 手部与持物：15张

目标：增强手部、道具、身份物件稳定性。

采集位：

| 序号 | Hand / Object          |
| -: | ---------------------- |
| 01 | empty hands            |
| 02 | holding scroll         |
| 03 | holding imperial edict |
| 04 | holding sword          |
| 05 | hand on sword hilt     |
| 06 | holding book           |
| 07 | holding brush          |
| 08 | hand resting on table  |
| 09 | adjusting sleeve       |
| 10 | raising hand           |
| 11 | pointing forward       |
| 12 | holding jade pendant   |
| 13 | holding cup            |
| 14 | folding hands          |
| 15 | opening scroll         |

Scene_Type：

```text
Character_Hand
```

---

## 10. G06 表情变化：10张

目标：让人物表情范围更稳定。

原则：

* 表情和动作分离。
* 图片表现表情。
* Caption 同时保留情绪词。

采集位：

| 序号 | Expression   |
| -: | ------------ |
| 01 | calm         |
| 02 | slight smile |
| 03 | serious      |
| 04 | determined   |
| 05 | thoughtful   |
| 06 | angry        |
| 07 | sad          |
| 08 | surprised    |
| 09 | worried      |
| 10 | relieved     |

Scene_Type：

```text
Character_Expression
```

---

## 11. G07 骑马增强：10张

目标：增强历史战争、草原、行军场景中的人物稳定性。

定位：

* 骑马不是核心身份采集位。
* 骑马是增强采集位。
* 适合辽、金、元、武将、骑兵人物。

风险：

* 可能让 LoRA 学到马、马鞍、缰绳。
* 因此骑马数量控制在 10 张。

采集位：

| 序号 | Horse Action               |
| -: | -------------------------- |
| 01 | riding horse still         |
| 02 | riding horse side view     |
| 03 | riding horse front view    |
| 04 | riding horse looking back  |
| 05 | riding horse holding reins |
| 06 | riding horse holding sword |
| 07 | galloping                  |
| 08 | riding horse medium shot   |
| 09 | riding horse full body     |
| 10 | riding horse distant shot  |

Scene_Type：

```text
Character_Horse
```

---

## 12. G08 场景参考：5张

目标：给后续 Qwen Image Edit、Flux、Wan、视频生成提供参考。

注意：

* 默认不进入 LoRA 训练。
* Dataset_Use = reference。
* 可带少量场景。

采集位：

| 序号 | Reference                     |
| -: | ----------------------------- |
| 01 | seated in court reference     |
| 02 | military camp reference       |
| 03 | grassland riding reference    |
| 04 | palace standing reference     |
| 05 | battlefield command reference |

Scene_Type：

```text
Character_Reference
```

---

## 13. 背景规则

训练图优先使用：

```text
white seamless background
simple neutral background
plain studio background
```

训练图避免：

```text
palace
court hall
battlefield
forest
sky
city
building
tent
crowd
throne
chair
```

例外：

G08 Reference 可以出现少量场景元素。

---

## 14. 动作与情绪映射规则

图片负责学习动作。

Caption 负责保留情绪语义。

示例：

```text
hands behind back
+
majestic
+
solemn
+
authoritative
```

这样未来用户输入：

```text
majestic emperor
```

LoRA 有机会回到：

```text
hands behind back
```

对应姿态。

---

## 15. Dataset_Plan 字段要求

每一行必须包含：

```text
Plan_ID
Character_ID
Group_ID
Group_Name
View_ID
Pose_ID
Posture_ID
Hand_ID
Expression_ID
Costume_ID
Template_ID
Scene_Type
Dataset_Use
Priority
Generate_Status
QC_Status
Notes
```

---

## 16. Dataset_Master 生成规则

Dataset_Master 不人工维护。

Dataset_Master 由 Dataset_Plan 自动生成。

每一行 Dataset_Plan 生成一行 Dataset_Master。

生成字段包括：

```text
Dataset_ID
Character_ID
File_Stem
Image_File
Caption_File
Metadata_File
Prompt_Positive
Prompt_Negative
Caption_Text
Width
Height
Aspect_Ratio
Model_Target
Dataset_Use
Train_Weight
Generate_Status
QC_Status
Train_Status
Notes
```

---

## 17. 文件命名规则

Dataset_ID：

```text
HC000001
```

File_Stem：

```text
HC000001_CHR0001_V001_P002_S001_H001_E003
```

生成文件：

```text
HC000001_CHR0001_V001_P002_S001_H001_E003.png
HC000001_CHR0001_V001_P002_S001_H001_E003.txt
HC000001_CHR0001_V001_P002_S001_H001_E003.json
```

---

## 18. Rule Engine 校验

生成 Dataset_Master 前必须校验：

* 所有 ID 是否存在。
* 动作与姿态是否允许组合。
* 手部动作是否适配姿态。
* 骑马类动作是否合理。
* Reference 是否被错误加入 train。

禁止静默生成非法组合。

非法组合示例：

```text
riding horse + kneeling
riding horse + hands clasped in front
sitting upright + galloping
standing + sitting upright
```

---

## 19. 第一版执行规则

第一版先生成：

```text
CHR_0001
```

共 100 行 Dataset_Plan。

不要人工写：

```text
Prompt_Positive
Caption_Text
Image_File
Metadata_File
```

这些全部由 Generator 生成。

---

## 20. 最终原则

HCDS 不维护图片。

HCDS 不维护 Prompt。

HCDS 不维护 Caption。

HCDS 维护：

```text
Character
Attribute
Rule
Plan
Schema
```

其它全部自动生成。
