#!/usr/bin/env python3

from __future__ import annotations

import artifactory
import argparse
import re
import os
import dataclasses

token = 'cmVmdGtuOjAxOjAwMDAwMDAwMDA6OHg0Y2ljVWFBUURWdFk5SXc2NHBEOXQ1azFn'

@dataclasses.dataclass
class Version:
    major: int 
    minor: int
    bugfix: int 

    def to_str(self) -> str:
        return f'{self.major}.{self.minor}.{self.bugfix}'


def get_fuzzer_arti_path() -> artifactory.ArtifactoryPath:
    path = artifactory.ArtifactoryPath(
        'https://sinflairtest.jfrog.io/artifactory/fuzzing/tools/fuzzer',
        token=token
    )

    try:
        path.mkdir() 
    except OSError:
        # Folder exists already
        pass

    return path

def get_latest_arti_version(fuzzer_arti_path: artifactory.ArtifactoryPath) -> Version:
    latest_version = (0, 0, 0)

    package_name_regex = re.compile(r'^fuzzer-(?P<major>\d+).(?P<minor>\d+).(?P<bugfix>\d+).tar.gz$')

    for filepath in fuzzer_arti_path:
        if not filepath.is_file():
            continue

        match = package_name_regex.match(os.path.basename(filepath))

        if not match:
            continue

        version = (int(match.group('major')), int(match.group('minor')), int(match.group('bugfix')))

        if version > latest_version:
            latest_version = version
    
    print(f'{latest_version=}')

    return Version(*latest_version)

def bump_version(version: Version, bump: str) -> None:
    if bump == 'major':
        version.major += 1
    elif bump == 'minor':
        version.minor += 1
    else:
        version.bugfix += 1
    
    print(f'Uploading as {version=}')


def main() -> int:
    parser = argparse.ArgumentParser(description='Upload a new version of the fuzzer tool')
    parser.add_argument('--bump', choices=['major', 'minor', 'bugfix'], default='minor',
                        help='Increase one of the MAJOR.MINOR.BUGFIX version number. Default: minor.')
    args = parser.parse_args()

    fuzzer_arti_path = get_fuzzer_arti_path()

    version = get_latest_arti_version(fuzzer_arti_path)

    bump_version(version, args.bump)

    # Create dummy file
    fuzzer_filename = f'fuzzer-{version.to_str()}.tar.gz'
    with open(fuzzer_filename, 'w') as f:
        f.write(version.to_str())
    
    fuzzer_arti_path.deploy_file(fuzzer_filename)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
