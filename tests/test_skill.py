import json
import re
import struct
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "show-shape"
VIEWS = {"screen", "states", "flow", "modules", "ownership", "impact", "split"}


class ShowShapeTests(unittest.TestCase):
    def test_single_skill_and_manifest(self):
        self.assertEqual(
            sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")),
            ["show-shape"],
        )
        manifest = json.loads((ROOT / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "show-shape")
        self.assertEqual(manifest["repository"], "https://github.com/superuserkalo/show-shape")
        self.assertFalse(list(ROOT.glob("*/plugin.json")))

    def test_skill_contract(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---\n", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: show-shape$")
        self.assertRegex(frontmatter, r"(?m)^description: .+$")
        self.assertIn("## Route", text)
        self.assertIn("## Draw", text)
        self.assertIn("The reply is only those headed views.", text)

    def test_reference_routes_and_readme_links(self):
        text = (SKILL / "SKILL.md").read_text()
        routes = re.findall(r"`references/([a-z-]+)\.md`", text)
        self.assertEqual(set(routes), VIEWS)
        self.assertEqual(len(routes), len(VIEWS))
        self.assertEqual({path.stem for path in (SKILL / "references").glob("*.md")}, VIEWS)
        for view in VIEWS:
            reference = (SKILL / "references" / f"{view}.md").read_text()
            self.assertTrue(reference.startswith(f"# {view.capitalize()}\n"))
            self.assertIn("```text", reference)
        readme = (ROOT / "README.md").read_text()
        for link in re.findall(r"\]\((?!https?://)([^)]+)\)", readme):
            self.assertTrue((ROOT / link).is_file(), link)

    def test_readme_screenshot(self):
        readme = (ROOT / "README.md").read_text()
        image = "assets/show-shape-in-action.png"
        self.assertIn(f"]({image})", readme)
        self.assertLess(readme.index(f"]({image})"), readme.index("## Install"))
        data = (ROOT / image).read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(data[12:16], b"IHDR")
        width, height = struct.unpack(">II", data[16:24])
        self.assertGreaterEqual(width, 1200)
        self.assertGreaterEqual(height, 800)
        transcript = (ROOT / "docs/example.md").read_text()
        self.assertIn("### screen", transcript)
        self.assertIn("### states", transcript)

    def test_readme_install_and_scope(self):
        readme = (ROOT / "README.md").read_text()
        install = readme.split("## Install\n", 1)[1].split("## Use\n", 1)[0]
        self.assertIn("1. **With the [Skills CLI]", install)
        self.assertIn("2. **Copy the complete skill directory", install)
        self.assertIn("Or simply tell your agent to install the skill from", install)
        self.assertNotIn("## Contents and verification", readme)
        self.assertNotIn("rendered for this preview", readme)
        self.assertNotIn("Read the prompt and response as text", readme)


if __name__ == "__main__":
    unittest.main()
