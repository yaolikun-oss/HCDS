import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "generators" / "prompt_generator.py"
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
            "CostumeStyle": "Khitan Noble",
            "BodyPose": "Standing",
            "RightHand": "Holding Saber",
            "EyeState": "Open",
            "MouthState": "Closed",
        }
        record = prompt_generator.compile_prompt(row)
        self.assertEqual(record.record_id, "CHAR-1")
        self.assertIn("Yelu Abaoji", record.prompt)
        self.assertIn("appearance: Oval", record.prompt)
        self.assertIn("costume: Khitan Noble", record.prompt)
        self.assertIn("pose: Standing, Holding Saber", record.prompt)
        self.assertIn("expression: Open, Closed", record.prompt)

    def test_cli_generates_prompt_file_from_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "dataset.csv"
            output_path = Path(tmp) / "Prompt.txt"
            with input_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["CharacterId", "CanonicalName", "BodyPose"])
                writer.writeheader()
                writer.writerow({"CharacterId": "CHAR-2", "CanonicalName": "Test Character", "BodyPose": "Standing"})
            exit_code = prompt_generator.main(["--input", str(input_path), "--output", str(output_path)])
            self.assertEqual(exit_code, 0)
            text = output_path.read_text(encoding="utf-8")
            self.assertIn("## CHAR-2", text)
            self.assertIn("Test Character", text)
            self.assertIn("pose: Standing", text)


if __name__ == "__main__":
    unittest.main()
