"""Build a self-contained single-skill ZIP from the canonical nine workflows."""
import argparse
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('start-learn', 'explain-and-check', 'quiz-me', 'connect-to-what-you-know',
         'ask-me-questions', 'learn-by-doing', 'linked-notes', 'flashcards', 'assess')
OLD_ROUTING = "For Scenario A, load the selected skill's instructions through the application's skill mechanism and follow them. Command prefixes in examples are illustrative; use the application's supported invocation syntax. If the target skill is unavailable, name the missing dependency and ask the user to install it; do not invent its workflow."
NEW_ROUTING = "For Scenario A, read the selected bundled workflow through the routing table in the package's root SKILL.md and follow it in this session. All workflows are included; do not request another skill installation. If a bundled file is inaccessible, name it and request access rather than inventing its workflow."


def files(root=ROOT):
    result = {'SKILL.md': (root / 'packaging/agensi/SKILL.md').read_bytes(),
              'references/SOURCES.md': (root / 'docs/sources.md').read_bytes(),
              'LICENSE': (root / 'LICENSE').read_bytes()}
    command = re.compile(r'(?<![\w/.-])/(?:' + '|'.join(NAMES) + r')\b')
    for name in NAMES:
        folder = root / 'skills' / name
        body = (folder / 'SKILL.md').read_text().split('---', 2)[2].lstrip()
        if name == 'start-learn':
            if body.count(OLD_ROUTING) != 1:
                raise ValueError('Canonical start-learn routing changed; review the bundle adapter')
            body = body.replace(OLD_ROUTING, NEW_ROUTING)
        resources = sorted(p for p in folder.glob('*.md') if p.name not in ('SKILL.md', 'SOURCES.md'))
        for resource in resources:
            body += f'\n\n<a id="{resource.stem.lower()}"></a>\n\n' + resource.read_text()
        for resource in resources:
            body = body.replace(f']({resource.name})', f'](#{resource.stem.lower()})')
        body = command.sub(lambda m: 'learn-skills: ' + m.group()[1:], body)
        body = body.replace('Suggested next: /<skill> <arguments>',
                            'Suggested next: learn-skills: <workflow> <arguments>')
        body = body.replace('as specified in `SKILL.md`',
                            'as specified in the protocol above')
        result[f'references/{name}.md'] = body.encode()
    return result


def build(output, root=ROOT):
    content = files(root)
    if output.exists():
        raise FileExistsError(f'Output already exists: {output}; choose a fresh path')
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(content.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/learn-skills-agensi.zip')
    print(build(parser.parse_args().output))
