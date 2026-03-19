CREATE TABLE fact_rag_retrieval_doc (
    query_id              UUID,
    doc_rank              INT,
    document_id           VARCHAR(200),
    source_path           VARCHAR(500),
    chunk_id              VARCHAR(200),
    similarity_score      FLOAT,
    chunk_length_chars    INT,
    PRIMARY KEY (query_id, doc_rank)
);