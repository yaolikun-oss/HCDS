# HCDS Generators

This directory contains implementation tooling derived from the HCDS specifications.

## Prompt Generator MVP

Generate prompt text from a logical dataset table:

```bash
python3 generators/prompt_generator.py \
  --input datasets/examples/HCDS_Master_MVP.csv \
  --output outputs/prompt_mvp.txt
```

Supported input formats:

* `.xlsx`
* `.csv`
* `.tsv`

The generator compiles currently frozen core entities into observable prompt fragments:

* Identity
* Appearance
* Costume
* Pose & Action
* Expression

The output is deterministic text intended as the first MVP bridge from Dataset Master to Prompt.
