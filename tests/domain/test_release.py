import json
from pathlib import Path

from com.xebialabs.xlrelease.domain import Release


def test_release_json():
    # Load release.json
    test_dir = Path(__file__).parent
    release_json_path = test_dir / "release.json"

    with open(release_json_path, 'r') as f:
        release_dict = json.load(f)

    # Parse JSON into Release model
    release = Release.from_dict(release_dict)

    # Check Release
    assert release is not None
    assert release.type == "xlrelease.Release"
    assert release.title == "TEST Release"
    assert release.id == "Applications/Folder856d5b08c3474414b1856e15bf06369e/Release34b169be50684b2ba5489a9099903bc4"

    # Check Phases
    phases = release.phases
    assert len(phases) == 1
    phase = phases[0]
    assert phase.title == "New Phase"

    # Check Tasks
    assert len(phase.tasks) >= 1
    task = phase.tasks[0]
    assert task.title == "Get release"

    # Check access of properties are present in the JSON but not in the model
    assert task.capabilities == ["remote"]
