import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "generators" / "prompt_generator.py"
EXAMPLE_DATASET = ROOT / "datasets" / "examples" / "HCDS_Master_MVP.csv"
spec = importlib.util.spec_from_file_location("prompt_generator", MODULE_PATH)
prompt_generator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = prompt_generator
spec.loader.exec_module(prompt_generator)


class PromptGeneratorTests(unittest.TestCase):
    def test_compile_prompt_from_core_entities(self):
        row = {
            "CharacterId": "CHAR-1",
            "CanonicalName": "Yelu Abaoji",
            "Dynasty": "Liao",
            "HistoricalRole": "Emperor",
            "FaceShape": "Oval",
            "CostumeStyle": "Khitan Round-Collar Robe",
            "BodyPose": "Standing",
            "RightHand": "Holding Saber",
            "EyeState": "Open",
            "MouthState": "Closed",
        }
        record = prompt_generator.compile_prompt(row)
        self.assertEqual(record.record_id, "CHAR-1")
        self.assertIn("Yelu Abaoji", record.prompt)
        self.assertIn("appearance: Oval", record.prompt)
        self.assertIn("costume: Khitan Round-Collar Robe", record.prompt)
        self.assertIn("pose: Standing, Holding Saber", record.prompt)
        self.assertIn("expression: Open, Closed", record.prompt)

    def test_rejects_interpretive_terms(self):
        row = {
            "CharacterId": "CHAR-2",
            "CanonicalName": "Example Character",
            "BodyPose": "Heroic",
        }
        with self.assertRaises(ValueError) as ctx:
            prompt_generator.compile_prompt(row)
        self.assertIn("Observable Principle violation", str(ctx.exception))
        self.assertIn("Heroic", str(ctx.exception))

    def test_dataset_to_prompt_to_output_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "Prompt.txt"
            exit_code = prompt_generator.main([
                "--input",
                str(EXAMPLE_DATASET),
                "--output",
                str(output_path),
            ])
            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.exists())
            text = output_path.read_text(encoding="utf-8")
            self.assertIn("## CHAR-0001", text)
            self.assertIn("Yelu Abaoji", text)
            self.assertIn("costume: Khitan Round-Collar Robe", text)
            self.assertIn("pose: Standing", text)
            self.assertIn("expression: Open", text)
            self.assertIn("## Error Report", text)
            self.assertIn("Skipped records: none", text)

    def test_batch_skips_invalid_records_and_keeps_valid_output(self):
        rows = [
            {
                "CharacterId": "CHAR-GOOD-1",
                "CanonicalName": "Valid One",
                "BodyPose": "Standing",
            },
            {
                "CharacterId": "CHAR-BAD",
                "CanonicalName": "Invalid One",
                "BodyPose": "Heroic",
            },
            {
                "CharacterId": "CHAR-GOOD-2",
                "CanonicalName": "Valid Two",
                "BodyPose": "Sitting",
            },
        ]
        result = prompt_generator.compile_batch(rows)
        self.assertEqual([record.record_id for record in result.prompts], ["CHAR-GOOD-1", "CHAR-GOOD-2"])
        self.assertEqual(len(result.skipped), 1)
        self.assertEqual(result.skipped[0].record_id, "CHAR-BAD")
        self.assertIn("Observable Principle violation", result.skipped[0].reason)

    def test_output_includes_skipped_record_report(self):
        records = [prompt_generator.PromptRecord("CHAR-GOOD", "Valid prompt")]
        skipped = [prompt_generator.SkippedRecord(2, "CHAR-BAD", "invalid value")]
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "Prompt.txt"
            prompt_generator.write_prompts(records, output_path, skipped=skipped)
            text = output_path.read_text(encoding="utf-8")
            self.assertIn("## CHAR-GOOD\nValid prompt", text)
            self.assertIn("## Error Report", text)
            self.assertIn("- row 2, CHAR-BAD: invalid value", text)


if __name__ == "__main__":
    unittest.main()
