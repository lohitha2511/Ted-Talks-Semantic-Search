# 🎤 TED Talk Recommender

This is a **Streamlit** application that recommends TED Talks based on a user-provided query. It uses **semantic search** to find the most relevant talks, allowing users to discover content based on topics, phrases, or keywords rather than just title matches.

## ✨ Features

* **Semantic Search**: Utilizes a pre-trained **Sentence Transformer** model (`all-MiniLM-L6-v2`) to embed both the TED Talk transcripts and the user query, enabling context-aware recommendations.
* **Efficient Indexing**: Uses a **FAISS (Facebook AI Similarity Search)** (`faiss-cpu`) index for fast and scalable similarity search across the entire dataset of TED Talks.
* **Intuitive UI**: Built with Streamlit, the app provides a simple and clean user interface for entering queries and displaying results.
* **Responsive Design**: The UI is designed with a card-based layout using custom CSS to look good on different screen sizes and supports both light and dark modes.

## 🚀 How It Works

The application operates in two main stages:

1.  **Data Preparation and Indexing**:
    * A dataset of TED Talks is used, which is pre-processed by cleaning the text within and removing unnecessary features.
    * The `title`, `details` (description), and `speaker` of each talk are concatenated into a single string.
    * The Sentence Transformer model converts these strings into high-dimensional numerical vectors, also known as embeddings.
    * A FAISS index is built from these embeddings, allowing for efficient nearest-neighbor search. This index and the embeddings are saved to disk.

2.  **Recommendation Engine (at runtime)**:
    * When a user enters a query, the same Sentence Transformer model converts it into a vector.
    * The FAISS index is queried to find the `k` most similar talk vectors to the query vector. Similarity is measured by **cosine similarity** (dot product on L2-normalized vectors).
    * The corresponding TED Talk details for the most similar vectors are retrieved and displayed to the user in an organized, card-based format.

---

## 🛠️ Project Structure

The project includes two main scripts:

* `TedTalks.py`: This is the main Streamlit application file. It loads the pre-built FAISS index and embeddings, handles user input, and displays the recommendations.
* `TedTalksEmbeddingBuilder.py`: This script is used to pre-process the data and create the FAISS index and embeddings. It includes functions for data cleaning, text embedding, index creation, and saving the necessary files. This part of the code is not run by the Streamlit app itself but is a prerequisite for its functionality.

## 📦 Requirements

To run this application, you need to install the following libraries:

```pip install streamlit pandas faiss-cpu sentence-transformers numpy scikit-learn matplotlib umap-learn```

Note: If you are on an NVIDIA GPU machine, you can install `faiss-gpu` for faster index building and querying.

## 🏃 Getting Started

1.  **Clone the repository:**
    ```
    git clone https://github.com/lohitha2511/Ted-Talks-Semantic-Search.git
    ```

2. **Build the embeddings and the index:**
   * Run the script in `TedTalksEmbeddingBuilder.ipynb` to build the embeddings and the similarity index from them, which will generate the required files in a folder called `/ted_index`. 
    
3.  **Run the Streamlit app:**
    ```
    streamlit run TedTalks.py
    ```
    This will launch the application in your web browser.
"""
