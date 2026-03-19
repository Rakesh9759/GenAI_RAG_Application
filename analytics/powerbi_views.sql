SELECT
    date(request_ts) as date,
    COUNT(*) as query_volume,
    AVG(total_latency_ms) as avg_latency,
    SUM(CASE WHEN status='error' THEN 1 ELSE 0 END) as errors
FROM fact_rag_query
GROUP BY date(request_ts)
ORDER BY date(request_ts);