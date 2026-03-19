SELECT
    request_date,
    COUNT(*) AS query_volume,
    AVG(total_latency_ms) AS avg_latency_ms,
    AVG(retrieval_latency_ms) AS avg_retrieval_latency_ms,
    AVG(generation_latency_ms) AS avg_generation_latency_ms,
    SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) AS success_count,
    SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) AS error_count
FROM fact_rag_query
GROUP BY request_date
ORDER BY request_date;