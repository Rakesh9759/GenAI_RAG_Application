import time
from src.telemetry import log_query, new_query_id, now


def ask_rag(query, qa_chain, vectorstore):
    qid = new_query_id()

    start_total = time.time()

    try:
        start_r = time.time()
        docs = vectorstore.similarity_search(query, k=4)
        retrieval_latency = int((time.time() - start_r) * 1000)

        start_g = time.time()
        result = qa_chain.invoke({"query": query})
        generation_latency = int((time.time() - start_g) * 1000)

        total_latency = int((time.time() - start_total) * 1000)

        answer = result["result"]

        log_query({
            "query_id": qid,
            "request_ts": now(),
            "query_text": query,
            "retrieval_latency_ms": retrieval_latency,
            "generation_latency_ms": generation_latency,
            "total_latency_ms": total_latency,
            "docs_returned": len(docs),
            "status": "success",
            "response_length": len(answer)
        })

        return answer

    except Exception as e:

        total_latency = int((time.time() - start_total) * 1000)

        log_query({
            "query_id": qid,
            "request_ts": now(),
            "query_text": query,
            "retrieval_latency_ms": None,
            "generation_latency_ms": None,
            "total_latency_ms": total_latency,
            "docs_returned": 0,
            "status": "error",
            "response_length": 0
        })

        raise e