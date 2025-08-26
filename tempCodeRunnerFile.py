
# if query:
#     with st.spinner("Searching TED Talks..."):
#         results = search_talks(query, top_k=top_k)

#     st.subheader(f"Recommendations for: *{query}*")

#     cols = st.columns(2, gap="large")
#     for i, r in enumerate(results):
#         with cols[i % 2]:
#             st.markdown(
#                 f"""
#                 <div style="border-radius:15px; padding:15px; margin-bottom:20px; 
#                             box-shadow: 0 4px 10px rgba(0,0,0,0.15); background-color:#2b2b2b;">
#                     <h4 style="margin-bottom:5px;">
#                         <a href="{r['url']}" target="_blank" style="text-decoration:none; color:#E62B1E;">
#                             {r['title']}
#                         </a>
#                     </h4>
#                     <p><b>👤 Speaker:</b> {r['speaker']}</p>
#                     <p style="color:#8c8c8c;">{r['details']}</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#             print(r['details'])