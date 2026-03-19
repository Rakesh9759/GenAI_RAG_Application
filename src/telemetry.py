import sqlite3
import uuid
import time
from datetime import datetime

DB = "rag_metrics.db"


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS fact_rag_query (
        query_id TEXT PRIMARY KEY,
        request_ts TEXT,
        query_text TEXT,
        retrieval_latency_ms INTEGER,
        generation_latency_ms INTEGER,
        total_latency_ms INTEGER,
        docs_returned INTEGER,
        status TEXT,
        response_length INTEGER
    )
    """)
    conn.commit()
    conn.close()


def log_query(payload):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO fact_rag_query VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        payload["query_id"],
        payload["request_ts"],
        payload["query_text"],
        payload["retrieval_latency_ms"],
        payload["generation_latency_ms"],
        payload["total_latency_ms"],
        payload["docs_returned"],
        payload["status"],
        payload["response_length"]
    ))
    conn.commit()
    conn.close()


def new_query_id():
    return str(uuid.uuid4())


def now():
    return datetime.utcnow().isoformat()