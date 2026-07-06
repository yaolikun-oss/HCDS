# Dataset Review Notes

State: MVP dataset implemented, Excel workbook placeholder pending.

The current working Dataset -> Prompt path uses:

```text
datasets/examples/HCDS_Master_MVP.csv
        ↓
generators/prompt_generator.py
        ↓
outputs/prompt_mvp.txt
```

The implementation-facing schema is copied from `schemas/HCDS_Master_Schema.md`.

The following `.xlsx` files remain 0-byte placeholders and are not valid Excel workbooks yet:

- HCDS_Master.xlsx
- Attribute_Library.xlsx
- Prompt_Template.xlsx

Non-implemented workbook placeholders outside the active MVP path were removed during Stabilization v1.2.
