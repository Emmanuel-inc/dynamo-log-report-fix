import json
import re
from collections import Counter
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
LOG_PATH = Path("/app/access.log")

REQUEST_RE = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')


def expected_values():
    """Compute the ground truth directly from the log so the checks stay honest."""
    paths, ips, total = Counter(), set(), 0
    for line in LOG_PATH.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = REQUEST_RE.search(line)
        if m:
            paths[m.group(1)] += 1
    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def load_report():
    assert REPORT_PATH.exists(), "no /app/report.json found"
    return json.loads(REPORT_PATH.read_text())


def test_report_is_valid_json_object():
    """Success criterion 1. The report file exists and parses as a single JSON object."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_has_exactly_expected_keys():
    """Success criterion 2. The object has exactly the three required keys."""
    report = load_report()
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"unexpected keys {sorted(report.keys())}"
    )


def test_total_requests_correct():
    """Success criterion 3. total_requests equals the number of non empty log lines."""
    report = load_report()
    assert report["total_requests"] == expected_values()["total_requests"]


def test_unique_ips_correct():
    """Success criterion 4. unique_ips equals the number of distinct client IPs."""
    report = load_report()
    assert report["unique_ips"] == expected_values()["unique_ips"]


def test_top_path_correct():
    """Success criterion 5. top_path equals the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == expected_values()["top_path"]
