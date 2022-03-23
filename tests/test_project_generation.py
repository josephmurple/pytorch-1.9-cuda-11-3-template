"""
Pytest 를 실행할 때, 프로젝트 roo_directory 를 Working Directory 로 설정해주세요.
"""

import os
import re
from binaryornot.check import is_binary


RE_OBJ = re.compile('{{(\s?cookiecutter)[.](.*?)}}')


def build_files_list(root_dir):
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, 'r', encoding="latin-1"):
            match = RE_OBJ.search(line)
            msg = 'variable not replaced in {}'
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context={}):
    """ 아무런 설정이 없을 때, 생성된 project_name 이 'template-project' (default 값) 인지 확인 """
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'template-project'
    assert result.project.isdir()
    paths = build_files_list(str(result.project))

    assert paths
    check_paths(paths)


def test_bake_custom_project(cookies):
    """ 사용자가 project_name 을 명시했을 경우, 의도한 대로 제대로 동작하는지 확인 """
    result = cookies.bake(extra_context={"project_name": "HELLO WORLD"})
    print(f"result: {result.project_path}")

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "hello-world"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename == "hello-world"
    assert result.project.isdir()
