There is an Apache style access log at `/app/access.log`. Read it and write a small
JSON summary of the traffic to `/app/report.json`.

The report must be a single JSON object with exactly three keys. `total_requests`
holds an integer, `unique_ips` holds an integer and `top_path` holds a string.

## Success criteria

1. The file `/app/report.json` exists and parses as a single JSON object.
2. The object has exactly the keys `total_requests`, `unique_ips` and `top_path`,
   nothing more and nothing less.
3. `total_requests` equals the number of non empty lines in `/app/access.log`.
4. `unique_ips` equals the number of distinct client IP addresses in the log,
   where the client IP is the first field on each line.
5. `top_path` equals the request path that appears most often in the log, taken
   from the quoted request line, for example `/index.html`.
