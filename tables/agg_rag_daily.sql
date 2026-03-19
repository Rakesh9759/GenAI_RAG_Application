CREATE VIEW agg_rag_daily AS
SELECT
    request_date,
    COUNT(*) AS query_volume,
    AVG(total_latency_ms) AS avg_total_latency_ms,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_latency_ms) AS p95_latency_ms,
    SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) AS success_count,
    SUM(CASE WHEN status <> 'success' THEN 1 ELSE 0 END) AS error_count,
    AVG(total_tokens) AS avg_tokens,
    SUM(total_tokens) AS total_tokens
FROM fact_rag_query
GROUP BY request_date;