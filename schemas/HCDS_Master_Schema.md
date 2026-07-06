# HCDS Master Schema

Version: v2.0 RC1
Status: Frozen Draft
Owner: User
Architect: ChatGPT
Consumers: Claude Code, Codex, Python, ComfyUI, OneTrainer

---

## 1. Core Rule

HCDS is schema-driven.

Excel is only one implementation.

All generators must follow this schema.

Do not hardcode prompts, captions, filenames, or metadata.

---

## 2. Master Workbook

Default implementation:

```text
datasets/HCDS_Master.xlsx
```

The workbook contains four layers:

```text
Character Layer
Attribute Layer
Rule Layer
Generator Layer
```

---

## 3. Required Sheets

### 3.1 Config

Global project configuration.

Required fields:

```text
Config_Key
Config_Value
Description
```

---

### 3.2 Character_Profile

Stores character identity.

Required fields:

```text
Character_ID
Character_Name_CN
Character_Name_EN
Character_Token
Dynasty
Period
Role_Type
Gender
Age_Range
Body_Type
Face_Feature
Default_Costume_ID
Default_Identity_Tags
Default_Style_Tags
Status
Notes
```

---

### 3.3 Attribute_View

Stores camera/view attributes.

Required fields:

```text
View_ID
View_Name_CN
View_Name_EN
Prompt_Tag
Caption_Tag
Camera_Type
Is_Core
Priority
Notes
```

---

### 3.4 Attribute_Pose

Stores body pose/action attributes.

Required fields:

```text
Pose_ID
Pose_Name_CN
Pose_Name_EN
Prompt_Tag
Caption_Tag
Emotion_Tags
Allowed_Posture
Forbidden_Posture
Is_Core
Priority
Notes
```

---

### 3.5 Attribute_Posture

Stores body state.

Required fields:

```text
Posture_ID
Posture_Name_CN
Posture_Name_EN
Prompt_Tag
Caption_Tag
Category
Is_Core
Priority
Notes
```

Examples:

```text
standing
sitting upright
walking
riding horse
kneeling
```

---

### 3.6 Attribute_Hand

Stores hand action and held objects.

Required fields:

```text
Hand_ID
Hand_Name_CN
Hand_Name_EN
Prompt_Tag
Caption_Tag
Held_Object
Emotion_Tags
Allowed_Posture
Forbidden_Posture
Is_Core
Priority
Notes
```

---

### 3.7 Attribute_Expression

Stores facial expression.

Required fields:

```text
Expression_ID
Expression_Name_CN
Expression_Name_EN
Prompt_Tag
Caption_Tag
Emotion_Tags
Is_Core
Priority
Notes
```

---

### 3.8 Attribute_Costume

Stores costume style.

Required fields:

```text
Costume_ID
Costume_Name_CN
Costume_Name_EN
Dynasty
Role_Type
Prompt_Tag
Caption_Tag
Is_Default
Notes
```

---

### 3.9 Emotion_Mapping

Maps observable actions to semantic emotion words.

Required fields:

```text
Mapping_ID
Source_Type
Source_ID
Emotion_Tag
User_Prompt_Word_CN
User_Prompt_Word_EN
Weight
Notes
```

Example:

```text
Pose_ID = P002
Action = hands behind back
Emotion_Tag = majestic, solemn, authoritative
```

---

### 3.10 Rule_Engine

Defines legal and illegal combinations.

Required fields:

```text
Rule_ID
Rule_Type
Source_Type
Source_ID
Target_Type
Target_ID
Action
Severity
Reason_CN
Reason_EN
```

Allowed values for Action:

```text
ALLOW
FORBID
WARN
```

---

### 3.11 Prompt_Template

Stores prompt templates.

Required fields:

```text
Template_ID
Template_Name
Model_Target
Positive_Template
Negative_Template
Background_Tag
Camera_Tag
Quality_Tag
Status
Notes
```

---

### 3.12 Dataset_Plan

Human-maintained dataset generation plan.

This is not final output.

Required fields:

```text
Plan_ID
Character_ID
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

### 3.13 Dataset_Master

Generated dataset index.

This sheet may be generated automatically from Dataset_Plan.

Required fields:

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

## 4. ID Rules

### Character_ID

Format:

```text
CHR_0001
```

### Dataset_ID

Format:

```text
HC000001
```

### Attribute IDs

```text
V001 = View
P001 = Pose
S001 = Posture
H001 = Hand
E001 = Expression
C001 = Costume
T001 = Template
R001 = Rule
```

---

## 5. File Naming Rule

File stem must be generated from Dataset_ID.

Required format:

```text
HC000001_CHR0001_V001_P002_S001_H001_E003
```

Generated files:

```text
HC000001_CHR0001_V001_P002_S001_H001_E003.png
HC000001_CHR0001_V001_P002_S001_H001_E003.txt
HC000001_CHR0001_V001_P002_S001_H001_E003.json
```

---

## 6. Caption Rule

Caption must include:

```text
Character_Token
Identity tags
Observable action tags
Posture tags
Hand tags
Expression tags
Emotion tags
Costume tags
```

Example:

```text
ylabj, historical Chinese emperor, standing, hands behind back, serious expression, majestic, solemn, authoritative, Liao dynasty costume
```

---

## 7. Generator Rule

Generators must read:

```text
Character_Profile
Attribute_* sheets
Emotion_Mapping
Rule_Engine
Prompt_Template
Dataset_Plan
```

Generators must output:

```text
Dataset_Master
Images
Captions
Metadata
ComfyUI batch files
OneTrainer dataset
```

---

## 8. Forbidden Practices

Do not manually maintain Prompt files.

Do not manually maintain Caption files.

Do not manually rename image files.

Do not invent fields.

Do not rename schema columns.

Do not delete schema columns.

Do not bypass Rule_Engine.

---

## 9. Extension Rule

New fields may be added only after RFC approval.

Existing fields must remain backward compatible.

Breaking changes require version update.
