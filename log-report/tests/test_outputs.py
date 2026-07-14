import json
import re
from collections import Counter
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
LOG_PATH = Path("/app/access.log")

REQUEST_RE = re.compile(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ')


def expected_values():
    """Compute ground truth straight from the log so the tests stay honest."""
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
    return json.loads(REPORT_PATH.read_text())


def test_report_exists_and_is_valid_json():
    """Criterion 1. /app/report.json exists and contains valid JSON."""
    assert REPORT_PATH.exists(), "no /app/report.json found"
    load_report()


def test_report_is_object_with_exactly_the_three_keys():
    """Criterion 2. The JSON is an object with exactly the three required keys."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"unexpected keys {sorted(report.keys())}"
    )


def test_total_requests_matches_the_log():
    """Criterion 3. total_requests equals the number of nonempty log lines."""
    assert load_report()["total_requests"] == expected_values()["total_requests"]


def test_unique_ips_matches_the_log():
    """Criterion 4. unique_ips equals the number of distinct client IPs."""
    assert load_report()["unique_ips"] == expected_values()["unique_ips"]


def test_top_path_matches_the_log():
    """Criterion 5. top_path equals the most frequently requested path."""
    assert load_report()["top_path"] == expected_values()["top_path"]
