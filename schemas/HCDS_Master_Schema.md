# HCDS Master Schema

Version: v2.0 MVP
Status: Implementation Aligned
Owner: HCDS Engineering

---

# 1. Purpose

This file defines the current implemented HCDS Master dataset schema used by the Prompt Generator MVP.

It is an implementation-facing schema alignment document. It reconciles the logical HCDS specifications with the fields currently consumed by `generators/prompt_generator.py`.

This file does not introduce new architecture.

---

# 2. MVP Dataset Shape

The current MVP uses one flat logical dataset table.

Canonical dataset path:

```text
datasets/examples/HCDS_Master_MVP.csv
```

The same field model MAY be represented as `.xlsx`, `.csv`, or `.tsv` when consumed by the Prompt Generator MVP.

The active MVP dataset shape is:

```text
HCDS_Master
        ↓
Dataset row
        ↓
Prompt record
```

# 3. Canonical MVP Fields

The MVP dataset fields are aligned with `FIELD_ALIASES` in `generators/prompt_generator.py`.

## 3.1 Identity Fields

| Canonical Field | Accepted Aliases | Prompt Role |
| --- | --- | --- |
| CharacterId | RecordId, ID, Id | Prompt record identifier |
| CanonicalName | CharacterName, Name | Identity prompt fragment |
| Dynasty | - | Identity prompt fragment |
| HistoricalRole | OfficialTitle, Role | Identity prompt fragment |

## 3.2 Appearance Fields

| Canonical Field | Accepted Aliases |
| --- | --- |
| BiologicalSex | Sex |
| EstimatedAge | AgeGroup, Age |
| FaceShape | - |
| EyeShape | - |
| EyeColor | - |
| EyebrowShape | - |
| NoseShape | - |
| MouthShape | - |
| HairStyle | - |
| HairLength | - |
| HairColor | - |
| BeardStyle | - |
| MustacheStyle | - |
| BodyBuild | - |
| HeightCategory | - |
| SkinTone | - |

## 3.3 Costume Fields

| Canonical Field | Accepted Aliases |
| --- | --- |
| CostumeStyle | - |
| Headwear | - |
| UpperGarment | - |
| LowerGarment | - |
| Footwear | - |
| Belt | - |
| Accessories | - |
| Armor | - |
| PrimaryWeapon | - |
| SecondaryWeapon | - |

## 3.4 Pose Fields

| Canonical Field | Accepted Aliases |
| --- | --- |
| BodyPose | - |
| HeadDirection | - |
| LeftArm | - |
| RightArm | - |
| LeftHand | - |
| RightHand | - |
| LeftLeg | - |
| RightLeg | - |
| InteractionObject | - |

## 3.5 Expression Fields

| Canonical Field | Accepted Aliases |
| --- | --- |
| EyeState | - |
| EyeDirection | - |
| EyebrowState | - |
| MouthState | - |
| FacialTension | - |

---

# 4. Dataset to Prompt Mapping

The Prompt Generator MVP compiles each dataset row into one prompt record.

| Prompt Section | Source Fields |
| --- | --- |
| Record Header | CharacterId or fallback CanonicalName |
| Identity | CanonicalName, Dynasty, HistoricalRole |
| appearance | BiologicalSex, EstimatedAge, FaceShape, EyeShape, EyeColor, EyebrowShape, NoseShape, MouthShape, HairStyle, HairLength, HairColor, BeardStyle, MustacheStyle, BodyBuild, HeightCategory, SkinTone |
| costume | CostumeStyle, Headwear, UpperGarment, LowerGarment, Footwear, Belt, Accessories, Armor, PrimaryWeapon, SecondaryWeapon |
| pose | BodyPose, HeadDirection, LeftArm, RightArm, LeftHand, RightHand, LeftLeg, RightLeg, InteractionObject |
| expression | EyeState, EyeDirection, EyebrowState, MouthState, FacialTension |

Empty values and null-like values are omitted from output.

Duplicate prompt fragments are deduplicated while preserving source order.

---

# 5. Observable Principle Enforcement

The Prompt Generator MVP enforces the Observable Principle using lightweight prohibited-term validation.

Dataset values SHALL describe observable or historically factual data.

Interpretive style words are rejected before prompt output is written.

Examples of rejected values include:

* Heroic
* Noble
* Majestic
* Powerful
* Natural
* Brave
* Determined
* 威严
* 坚定
* 霸气

This validation is intentionally conservative and does not create a separate rule engine.

---

# 6. Supported Input Formats

The Prompt Generator MVP supports:

* `.csv`
* `.tsv`
* `.xlsx`

Reading `.xlsx` files requires `openpyxl`, declared in `requirements.txt`.

---

# 7. Current MVP Contract

The current end-to-end MVP contract is:

```text
datasets/examples/HCDS_Master_MVP.csv
        ↓
generators/prompt_generator.py
        ↓
outputs/prompt_mvp.txt
```

The generator SHALL NOT require non-implemented workbook layers.

The generator SHALL reject unsupported input formats.

The generator SHALL reject non-observable interpretive prompt values.

---

# 8. Known Deferred Items

The following are deferred and not required for the current MVP:

* physical Excel workbook layout
* full validator engine
* prompt template engine
* advanced validation engines
* aggregate profile implementation
* schema compiler

Deferred items MAY be implemented later only through dedicated specifications and implementation tasks.

---

# 9. End of Schema

This schema is aligned to the current working Dataset -> Prompt MVP implementation.

End of document.
