import json
import re
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
        for link in re.findall(r"\]\((skills/[^)]+)\)", readme):
            self.assertTrue((ROOT / link).is_file(), link)


if __name__ == "__main__":
    unittest.main()
