import os
import time

from src.telemetry import init_metrics_db, insert_query_log, new_query_id, utc_now_iso

init_metrics_db()

def ask_rag(qa, vectorstore, query: str, user_id: str = None, session_id: str = None) -> dict:
    query_id = new_query_id()
    start_total = time.perf_counter()

    retrieval_latency_ms = None
    generation_latency_ms = None
    docs_returned = 0
    answer = None

    try:
        # Retrieval timing
        start_retrieval = time.perf_counter()
        docs = vectorstore.similarity_search(query, k=4)
        retrieval_latency_ms = int((time.perf_counter() - start_retrieval) * 1000)
        docs_returned = len(docs)

        # Generation timing
        start_generation = time.perf_counter()
        result = qa.invoke({"query": query})
        generation_latency_ms = int((time.perf_counter() - start_generation) * 1000)

        answer = result.get("result") if isinstance(result, dict) else str(result)

        total_latency_ms = int((time.perf_counter() - start_total) * 1000)

        insert_query_log({
            "query_id": query_id,
            "request_ts": utc_now_iso(),
            "request_date": utc_now_iso()[:10],
            "user_id": user_id,
            "session_id": session_id,
            "environment": os.getenv("ENVIRONMENT", "dev"),
            "app_version": os.getenv("APP_VERSION", "1.0.0"),
            "query_text": query,
            "query_length_chars": len(query),
            "retrieval_k": 4,
            "docs_returned": docs_returned,
            "retrieval_latency_ms": retrieval_latency_ms,
            "generation_latency_ms": generation_latency_ms,
            "total_latency_ms": total_latency_ms,
            "model_name": "llama-2-7b-chat.ggmlv3.q2_K.bin",
            "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
            "vector_store": "pinecone",
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
            "status": "success",
            "error_type": None,
            "error_message": None,
            "response_length_chars": len(answer) if answer else 0,
            "answer_preview": answer[:500] if answer else None
        })

        return {"query_id": query_id, "answer": answer, "docs_returned": docs_returned}

    except Exception as exc:
        total_latency_ms = int((time.perf_counter() - start_total) * 1000)

        insert_query_log({
            "query_id": query_id,
            "request_ts": utc_now_iso(),
            "request_date": utc_now_iso()[:10],
            "user_id": user_id,
            "session_id": session_id,
            "environment": os.getenv("ENVIRONMENT", "dev"),
            "app_version": os.getenv("APP_VERSION", "1.0.0"),
            "query_text": query,
            "query_length_chars": len(query),
            "retrieval_k": 4,
            "docs_returned": docs_returned,
            "retrieval_latency_ms": retrieval_latency_ms,
            "generation_latency_ms": generation_latency_ms,
            "total_latency_ms": total_latency_ms,
            "model_name": "llama-2-7b-chat.ggmlv3.q2_K.bin",
            "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
            "vector_store": "pinecone",
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
            "status": "error",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "response_length_chars": 0,
            "answer_preview": None
        })
        raise