An Apache-style access log is located at `/app/access.log`. Parse it and produce a
small JSON summary report at `/app/report.json`.

The report must be a single JSON object with exactly these keys:

- `total_requests` (integer): the total number of non-empty log lines.
- `unique_ips` (integer): the number of distinct client IP addresses (the first
  field of each log line).
- `top_path` (string): the request path that appears most often in the log
  (the path portion of the quoted request line, e.g. `/index.html`).

## Success criteria

1. The file `/app/report.json` exists and contains valid JSON.
2. The JSON is an object with exactly the three keys `total_requests`,
   `unique_ips`, and `top_path`.
3. `total_requests` equals the number of non-empty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct client IPs in the log.
5. `top_path` equals the most frequently requested path in the log.
