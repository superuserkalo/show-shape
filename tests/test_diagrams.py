import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/show-shape/scripts/check_diagrams.py'
spec = importlib.util.spec_from_file_location('check_diagrams', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DiagramTests(unittest.TestCase):
    def test_every_reference_and_readme(self):
        paths = sorted((ROOT / 'skills/show-shape/references').glob('*.md'))
        paths.append(ROOT / 'README.md')
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(checker.check_markdown(path.read_text()), [])

    def test_valid_title_and_padded_body(self):
        self.assertEqual(checker.check_diagram(
            '┌─ Long title ─┐\n│ text         │\n│              │\n└──────────────┘'), [])

    def test_screenshot_style_jagged_right_edge(self):
        errors = checker.check_diagram(
            '┌─ Installed skill ──┐\n'
            '│ Workflow, legal text │\n'
            '│ playbook and dates │\n'
            '└────────────────────┘')
        self.assertTrue(any('box side' in error for error in errors))

    def test_long_repository_label_does_not_fit_old_frame(self):
        errors = checker.check_diagram(
            '┌─ skill ────────────┐\n'
            '│ scripts/check_updates.py │\n'
            '└────────────────────┘')
        self.assertTrue(any('box side' in error for error in errors))

    def test_shifted_inner_box_inside_valid_outer_box(self):
        text = ('┌────────────┐\n'
                '│ ┌────┐     │\n'
                '│ │ x   │    │\n'
                '│ └────┘     │\n'
                '└────────────┘')
        self.assertTrue(checker.check_diagram(text))

    def test_missing_corner_and_bottom_border(self):
        for text in ['┌────┐\n│ ok │\n└───┘',
                     '┌────┐\n│ ok │\n└─ ──┘',
                     '┌────┐\n│ ok │']:
            with self.subTest(text=text):
                self.assertTrue(checker.check_diagram(text))

    def test_arrow_tail_and_destination(self):
        valid = '┌───┐\n│ A │\n└─┬─┘\n  ▼\n┌───┐\n│ B │\n└───┘'
        self.assertEqual(checker.check_diagram(valid), [])
        for broken in [valid.replace('  ▼', '   ▼'),
                       valid.replace('  ▼\n', '  ▼\n\n'),
                       valid.replace('└─┬─┘', '└───┘')]:
            self.assertTrue(checker.check_diagram(broken))

    def test_branch_and_table_junctions(self):
        for view in ['ownership', 'split']:
            text = (ROOT / f'skills/show-shape/references/{view}.md').read_text()
            self.assertEqual(checker.check_markdown(text), [])
            junction = '┴' if view == 'ownership' else '┼'
            self.assertTrue(checker.check_markdown(text.replace(junction, '─', 1)))

    def test_width_uses_terminal_cells(self):
        text = '┌────┐\n│ 漢 │\n└────┘'
        self.assertEqual(checker.check_diagram(text, max_width=6), [])
        self.assertTrue(checker.check_diagram(text, max_width=5))
        self.assertEqual(checker.check_diagram(
            '┌───┐\n│ e\u0301 │\n└───┘', max_width=5), [])

    def test_tabs_and_absent_diagrams(self):
        self.assertTrue(checker.check_diagram('┌───┐\n│\tx│\n└───┘'))
        self.assertTrue(checker.check_markdown('No diagram.'))
        self.assertTrue(checker.check_markdown('```text\njust prose\n```'))

    def test_cli_stdin_and_file(self):
        valid = '```text\n┌───┐\n│ A │\n└───┘\n```\n'
        result = subprocess.run([sys.executable, str(SCRIPT)], input=valid,
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable, str(SCRIPT), '-'],
                                input=valid.replace('│ A │', '│ long label │'),
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('diagram 1:', result.stderr)
        result = subprocess.run([sys.executable, str(SCRIPT), '--max-width', '88',
                                 str(ROOT / 'README.md')], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_skill_requires_preflight_not_only_view_selection(self):
        text = (ROOT / 'skills/show-shape/SKILL.md').read_text()
        for requirement in ['88 display columns', 'Wrap long labels inside the box',
                            'including blank lines', 'scripts/check_diagrams.py',
                            'Without tools, count columns', 'Do not emit a known-broken diagram']:
            self.assertIn(requirement, text)


if __name__ == '__main__':
    unittest.main()
