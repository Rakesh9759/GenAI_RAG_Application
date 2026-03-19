SELECT
    substr(request_ts, 1, 13) AS request_hour,
    COUNT(*) AS query_volume,
    AVG(total_latency_ms) AS avg_latency_ms
FROM fact_rag_query
GROUP BY substr(request_ts, 1, 13)
ORDER BY request_hour;