import streamlit as st
import pandas as pd
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="TED Talk Recommender", page_icon="🎤", layout="centered")

st.markdown(
    """
    <style>
    .card {
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        background-color: #f9f9f9; /* default light mode */
        color: #333333;
    }
    .card h4 a {
        text-decoration: none;
        color: #DAA520; /* gold */
    }
    .card p {
        margin: 5px 0;
    }
    .card .details {
        color: #6e6e6e;
    }

    @media (prefers-color-scheme: dark) {
        .card {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        .card h4 a {
            color: #FFD700;
        }
        .card .details {
            color: #8c8c8c;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource
def load_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@st.cache_resource
def load_index_and_embeddings(path):
    index = faiss.read_index(os.path.join(path, "faiss_index.bin"))
    embs = np.load(os.path.join(path, "embeddings.npy"))
    df = pd.read_csv(os.path.join(path, "ted_processed.csv"))
    df['main_speaker'] = df['main_speaker'].fillna("Unknown Speaker")
    return index, embs, df

model = load_model()
index, embs, df = load_index_and_embeddings("ted_index")

def search_talks(query, top_k=5):
    query_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    D, I = index.search(query_emb, top_k)
    
    results = []
    for idx in I[0]:
        row = df.iloc[idx]
        results.append({
            "title": row['title'],
            "speaker": row['main_speaker'],
            "url": row['url'],
            "details": row['details'][:250].replace("\n", " ") + "..."
        })
    return results

st.title("🎤 TED Talk Recommender")
st.write("Find the most relevant TED Talks by entering a keyword, phrase, or topic.")

col1, col2 = st.columns([6, 1])

with col1:
    query = st.text_input("🔍 Enter a topic or phrase:", "", label_visibility="collapsed", placeholder="Enter a topic or keywords to search...")

with col2:
    top_k = st.selectbox(
        "Results",
        index=4,
        options=list(range(1, 11)), 
        label_visibility="collapsed",
        placeholder="No. of results"
    )

if query:
    with st.spinner("Searching TED Talks..."):
        results = search_talks(query, top_k=top_k)

    st.subheader(f"Recommendations for: *{query}*")

    cols = st.columns(2, gap="large")
    for i, r in enumerate(results):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <h4 style="margin-bottom:5px;">
                        <a href="{r['url']}" target="_blank">{r['title']}</a>
                    </h4>
                    <p><b>👤 Speaker:</b> {r['speaker']}</p>
                    <p class="details">{r['details']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
