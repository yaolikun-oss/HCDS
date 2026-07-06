# Costume Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect

---

# 1. Purpose

The Costume entity defines all clothing, armor, accessories, and carried equipment worn by a historical character.

Costume describes wearable objects only.

It SHALL NOT define:

* identity
* physical appearance
* pose
* facial expression
* camera
* scene

---

# 2. Domain Categories

The Costume entity consists of the following logical categories.

| Category      | Description                    |
| ------------- | ------------------------------ |
| Headwear      | Hats, crowns, helmets          |
| Upper Garment | Robes, coats, armor upper body |
| Lower Garment | Pants, skirts, robes           |
| Footwear      | Boots, shoes                   |
| Belt          | Belt, sash                     |
| Accessories   | Jewelry, ornaments, badges     |
| Armor         | Armor components               |
| Weapon        | Sword, bow, spear, etc.        |

---

# 3. Logical Fields

| Field           | Purpose                   |
| --------------- | ------------------------- |
| CostumeStyle    | Overall clothing style    |
| Headwear        | Head equipment            |
| UpperGarment    | Upper clothing            |
| LowerGarment    | Lower clothing            |
| Footwear        | Footwear                  |
| Belt            | Belt or sash              |
| Accessories     | Decorative accessories    |
| Armor           | Armor description         |
| PrimaryWeapon   | Main carried weapon       |
| SecondaryWeapon | Optional secondary weapon |

Field definitions SHALL follow the HCDS Field Model.

---

# 4. Constraints

Costume SHALL describe only wearable or carried objects.

Examples:

✓ Khitan round-collar robe

✓ Song dynasty court robe

✓ Iron lamellar armor

✓ Leather riding boots

The following are prohibited:

✗ Brave clothing

✗ Noble robe

✗ Heroic armor

because they describe interpretation rather than observable objects.

---

# 5. Independence

Changing Costume SHALL NOT modify:

* Identity
* Appearance
* Pose
* Expression

Different costumes MAY reuse the same Identity and Appearance.

---

# 6. Validation

Validation SHALL verify:

* required fields
* controlled vocabulary references
* logical consistency

Validation SHALL NOT evaluate artistic quality.

---

# 7. Example (Informative)

| Field         | Example              |
| ------------- | -------------------- |
| CostumeStyle  | Khitan Noble         |
| Headwear      | Black Fur Hat        |
| UpperGarment  | Dark Green Robe      |
| LowerGarment  | Matching Riding Robe |
| Footwear      | Leather Riding Boots |
| Belt          | Brown Leather Belt   |
| Armor         | None                 |
| PrimaryWeapon | Saber                |

---

# 8. Compliance

Implementations SHALL preserve:

* logical field semantics
* field ownership
* implementation independence

---

# 9. Freeze Decision

The Costume Model defined by this specification is frozen for HCDS v2.0.

---

# 10. End of Specification

This document defines the canonical Costume entity for HCDS v2.0.

End of document.
