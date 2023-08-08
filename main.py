#!/usr/bin/env python3

from __future__ import annotations

import artifactory
import os
import io
import zipfile

token = 'cmVmdGtuOjAxOjAwMDAwMDAwMDA6OHg0Y2ljVWFBUURWdFk5SXc2NHBEOXQ1azFn'

""" fuzzing:
- ccp
    - ocp
        - corpus
        - YYYY_MM_DD_HH_MM_SS
            - crashes
            - timeouts
            - _internal
        - runnable_summary.txt
    - subsys_summary.txt
- nfm
- summary.txt
"""

def main() -> int:
    subsys_name = 'ccp'
    runnables = ['ocp', 'aaa']
    date = '2023_06_10_07_32_55'
    # list of runnables

    fuzzing_arti_path_str = 'https://sinflairtest.jfrog.io/artifactory/fuzzing/123/fuzzing'

    subsys_arti_path_str = os.path.join(fuzzing_arti_path_str, subsys_name)

    subsys_arti_path = artifactory.ArtifactoryPath(subsys_arti_path_str, token=token)

    try:
        subsys_arti_path.mkdir()
    except OSError:
        # Folder exists already
        pass

    with subsys_arti_path.archive(archive_type='zip', check_sum=False).open() as subsys_arti:
        with zipfile.ZipFile(io.BytesIO(subsys_arti.read())) as zip_ref:
            zip_ref.extractall('/tmp/fuzzer/')

    return

    # probably create on remote first, then download -> not good if tooling crashes
    # only download for the runnables that are fuzzed? optimization. just download all for now

    # path = artifactory.ArtifactoryPath(
    #     os.path.join(fuzzing_arti_path, '1', '2', '3'),
    #     token=token
    # )

    try:
        path.mkdir() 
    except OSError:
        # Folder exists already
        pass

    
    #fuzzer_arti_path.deploy_file(fuzzer_filename)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
