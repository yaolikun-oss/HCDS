# Pose & Action Specification

Version: v2.0
Status: Frozen
Owner: HCDS Chief Architect

---

# 1. Purpose

The Pose entity defines the observable body posture and physical action of a historical character.

Pose describes only physical body configuration.

It SHALL NOT define:

* identity
* appearance
* costume
* facial expression
* camera
* scene
* emotion

---

# 2. Design Principle

Every pose SHALL be:

* Observable
* Measurable
* Reproducible

Abstract descriptions are prohibited.

Examples:

✓ Standing

✓ Walking

✓ Sitting

✓ Kneeling

✓ Horse Riding

Prohibited:

✗ Heroic

✗ Powerful

✗ Majestic

✗ Natural

These describe interpretation rather than body posture.

---

# 3. Domain Categories

| Category       | Description              |
| -------------- | ------------------------ |
| Body Pose      | Overall body posture     |
| Head Direction | Head orientation         |
| Left Arm       | Left arm position        |
| Right Arm      | Right arm position       |
| Left Hand      | Left hand action         |
| Right Hand     | Right hand action        |
| Left Leg       | Left leg position        |
| Right Leg      | Right leg position       |
| Interaction    | Interaction with objects |

---

# 4. Logical Fields

| Field             | Purpose                      |
| ----------------- | ---------------------------- |
| BodyPose          | Primary body posture         |
| HeadDirection     | Head orientation             |
| LeftArm           | Left arm position            |
| RightArm          | Right arm position           |
| LeftHand          | Left hand action             |
| RightHand         | Right hand action            |
| LeftLeg           | Left leg position            |
| RightLeg          | Right leg position           |
| InteractionObject | Object being held or touched |

Field definitions SHALL conform to the HCDS Field Model.

---

# 5. Constraints

Pose SHALL describe only observable body positions.

Examples:

✓ Both hands behind back

✓ Right hand holding sword

✓ Left hand holding scroll

✓ Sitting cross-legged

✓ Standing upright

Pose SHALL NOT contain:

✗ Calm

✗ Angry

✗ Noble

✗ Elegant

These belong to other entities.

---

# 6. Independence

Pose SHALL remain independent from:

* Identity
* Appearance
* Costume
* Expression

The same Pose MAY be reused across multiple costumes and characters.

---

# 7. Validation

Validation SHALL verify:

* logical completeness
* compatible body positions
* controlled vocabulary references

Impossible body configurations SHALL be rejected.

---

# 8. Example

| Field             | Example          |
| ----------------- | ---------------- |
| BodyPose          | Standing         |
| HeadDirection     | Forward          |
| LeftArm           | Relaxed          |
| RightArm          | Bent             |
| RightHand         | Holding Sword    |
| LeftHand          | Empty            |
| LeftLeg           | Straight         |
| RightLeg          | Slightly Forward |
| InteractionObject | Saber            |

---

# 9. Compliance

Implementations SHALL preserve:

* observable semantics
* implementation independence
* logical consistency

---

# 10. Freeze Decision

The Pose & Action Model defined by this specification is frozen for HCDS v2.0.

---

# 11. End of Specification

This document defines the canonical Pose & Action entity for HCDS v2.0.

End of document.
