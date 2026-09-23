import importlib.util
from pathlib import Path, PurePosixPath
import re
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_agensi', ROOT / 'scripts/build_agensi.py')
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)


class AgensiPackageTests(unittest.TestCase):
    def test_archive_is_self_contained_and_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = bundle.build(Path(tmp) / 'first.zip')
            second = bundle.build(Path(tmp) / 'second.zip')
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertIsNone(archive.testzip())
                names = archive.namelist()
                self.assertEqual([p for p in names if p.endswith('SKILL.md')], ['SKILL.md'])
                self.assertEqual(archive.read('references/SOURCES.md'), (ROOT / 'docs/sources.md').read_bytes())
                for name in bundle.NAMES:
                    self.assertIn(f'references/{name}.md', names)
                for name in names:
                    if not name.endswith('.md'):
                        continue
                    text = archive.read(name).decode()
                    prose = re.sub(r'^```[^\n]*\n.*?^```[^\n]*(?:\n|$)', '', text, flags=re.M | re.S)
                    for target in re.findall(r'\]\(([^)]+)\)', prose):
                        if re.match(r'[a-z][a-z0-9+.-]*:', target, re.I):
                            continue
                        path, _, anchor = target.partition('#')
                        resolved = str(PurePosixPath(name).parent / path) if path else name
                        self.assertIn(resolved, names, (name, target))
                        if anchor:
                            self.assertIn(f'id="{anchor}"', archive.read(resolved).decode())

    def test_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'existing.zip'
            path.write_bytes(b'keep')
            with self.assertRaises(FileExistsError):
                bundle.build(path)
            self.assertEqual(path.read_bytes(), b'keep')

    def test_rejects_stale_routing_adapter(self):
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ('skills', 'packaging', 'docs'):
                shutil.copytree(ROOT / folder, root / folder)
            shutil.copyfile(ROOT / 'LICENSE', root / 'LICENSE')
            path = root / 'skills/start-learn/SKILL.md'
            path.write_text(path.read_text().replace(bundle.OLD_ROUTING, 'Changed routing'))
            with self.assertRaisesRegex(ValueError, 'routing changed'):
                bundle.build(root / 'out.zip', root)
            self.assertFalse((root / 'out.zip').exists())
