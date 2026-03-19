CREATE TABLE fact_rag_query (
    query_id              UUID PRIMARY KEY,
    request_ts            TIMESTAMP NOT NULL,
    request_date          DATE NOT NULL,
    user_id               VARCHAR(100),
    session_id            VARCHAR(100),
    environment           VARCHAR(20),      -- dev/test/prod
    app_version           VARCHAR(50),

    query_text            TEXT,
    query_length_chars    INT,
    retrieval_k           INT,
    docs_returned         INT,

    retrieval_latency_ms  INT,
    generation_latency_ms INT,
    total_latency_ms      INT,

    model_name            VARCHAR(100),
    embedding_model       VARCHAR(100),
    vector_store          VARCHAR(50),

    prompt_tokens         INT,
    completion_tokens     INT,
    total_tokens          INT,

    status                VARCHAR(20),      -- success/error/timeout
    error_type            VARCHAR(100),
    error_message         TEXT,

    response_length_chars INT,
    answer_preview        TEXT
);