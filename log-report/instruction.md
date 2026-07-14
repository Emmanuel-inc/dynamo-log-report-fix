There is a web server access log at `/app/access.log`. Read it and write a short
JSON summary of the traffic to `/app/report.json`.

The report must be a single JSON object with exactly three keys.

- `total_requests` is an integer. It is the number of nonempty lines in the log.
- `unique_ips` is an integer. It is the number of distinct client IP addresses.
  The IP address is the first field on each log line.
- `top_path` is a string. It is the request path that appears most often in the
  log, for example `/index.html`. The path is the second word inside the quoted
  request portion of each line.

## Success criteria

1. The file `/app/report.json` exists and contains valid JSON.
2. The JSON is an object with exactly the keys `total_requests`, `unique_ips`
   and `top_path`.
3. `total_requests` equals the number of nonempty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct client IP addresses in the log.
5. `top_path` equals the most frequently requested path in the log.
