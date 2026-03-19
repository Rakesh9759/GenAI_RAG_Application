CREATE TABLE fact_rag_feedback (
    feedback_id           UUID PRIMARY KEY,
    query_id              UUID NOT NULL,
    feedback_ts           TIMESTAMP NOT NULL,
    user_id               VARCHAR(100),
    rating                VARCHAR(20),   
    feedback_text         TEXT
);