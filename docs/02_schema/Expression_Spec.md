# Expression Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect

---

# 1. Purpose

The Expression entity defines the observable facial expression of a historical character.

Expression describes only visible facial features.

It SHALL NOT define:

* identity
* appearance
* costume
* body pose
* camera
* scene
* internal thoughts

---

# 2. Design Principle

Every expression SHALL be observable.

Expression SHALL describe visible facial changes rather than emotional interpretation.

Examples:

✓ Mouth Closed

✓ Slight Smile

✓ Eyes Wide Open

✓ Eyebrows Slightly Raised

Prohibited:

✗ Brave

✗ Determined

✗ Loyal

✗ Wise

These describe interpretation rather than observable facial appearance.

---

# 3. Domain Categories

| Category       | Description                 |
| -------------- | --------------------------- |
| Eyes           | Eye openness and direction  |
| Eyebrows       | Eyebrow position            |
| Mouth          | Mouth shape                 |
| Facial Tension | Overall facial muscle state |

---

# 4. Logical Fields

| Field         | Purpose               |
| ------------- | --------------------- |
| EyeState      | Eye openness          |
| EyeDirection  | Viewing direction     |
| EyebrowState  | Eyebrow position      |
| MouthState    | Mouth shape           |
| FacialTension | Facial muscle tension |

Field definitions SHALL conform to the HCDS Field Model.

---

# 5. Constraints

Expression SHALL describe only observable facial characteristics.

Examples:

✓ Eyes Looking Forward

✓ Mouth Closed

✓ Slight Smile

✓ Neutral Eyebrows

Expression SHALL NOT describe:

✗ Courage

✗ Intelligence

✗ Kindness

✗ Majesty

Those belong to narrative interpretation rather than facial observation.

---

# 6. Independence

Expression SHALL remain independent from:

* Identity
* Appearance
* Costume
* Pose

The same expression MAY be reused across different costumes, poses, and scenes.

---

# 7. Validation

Validation SHALL verify:

* logical completeness
* compatible facial states
* controlled vocabulary references

Contradictory facial states SHALL be rejected.

---

# 8. Example

| Field         | Example |
| ------------- | ------- |
| EyeState      | Open    |
| EyeDirection  | Forward |
| EyebrowState  | Neutral |
| MouthState    | Closed  |
| FacialTension | Relaxed |

---

# 9. Compliance

Implementations SHALL preserve:

* observable facial semantics
* logical consistency
* implementation independence

---

# 10. Freeze Decision

The Expression Model defined by this specification is frozen for HCDS v2.0.

---

# 11. End of Specification

This document defines the canonical Expression entity for HCDS v2.0.

End of document.
