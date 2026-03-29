# import requests
# import pandas as pd
# import streamlit as st
# 
# st.set_page_config(page_title="Delta Exchange Funding Rates", layout="wide")
# st.title("📊 Delta Exchange – Funding Rate Scanner")
# 
# 
# # -----------------------------------
# # Fetch data from Delta Exchange API
# # -----------------------------------
# def fetch_data():
#     headers = {"Accept": "application/json"}
#     r = requests.get("https://api.india.delta.exchange/v2/tickers", headers=headers)
#     r.raise_for_status()
#     data = r.json()
#     return data.get("result", [])
# 
# 
# # -----------------------------------
# # Button to fetch & process data
# # -----------------------------------
# isClosed = True
# 
# if isClosed:
#     st.warning("This site has been permanantly shifted to https://aysm.in/fundings")
#     st.success("Thank you for your support till now, hope to see you in our new site 😊 ")
# 
# 
# elif st.button("🔄 Fetch Funding Rates"):
# 
#     with st.spinner("Fetching live data from Delta Exchange..."):
#         tickers = fetch_data()
# 
#     # -----------------------------------
#     # Extract coins with funding rates
#     # -----------------------------------
#     coins_with_funding = []
# 
#     for coin in tickers:
#         funding_rate = coin.get("funding_rate")
# 
#         if funding_rate is not None:
#             coins_with_funding.append(
#                 {
#                     "symbol": coin.get("symbol"),
#                     "underlying_asset_symbol": coin.get("underlying_asset_symbol"),
#                     "funding_rate": funding_rate,
#                     "mark_price": coin.get("mark_price"),
#                     "spot_price": coin.get("spot_price"),
#                     "oi_value_usd": coin.get("oi_value_usd"),
#                     "time": coin.get("time"),
#                 }
#             )
# 
#     # -----------------------------------
#     # Create DataFrame
#     # -----------------------------------
#     df = pd.DataFrame(coins_with_funding)
# 
#     if df.empty:
#         st.warning("No funding rate data found.")
#         st.stop()
# 
#     # Ensure funding_rate is numeric
#     df["funding_rate"] = pd.to_numeric(df["funding_rate"], errors="coerce")
#     df = df.dropna(subset=["funding_rate"])
# 
#     # -----------------------------------
#     # Split into positive & negative funding
#     # -----------------------------------
#     df_positive = (
#         df[df["funding_rate"] > 0]
#         .sort_values(by="funding_rate", ascending=False)
#         .reset_index(drop=True)
#     )
# 
#     df_negative = (
#         df[df["funding_rate"] < 0]
#         .sort_values(by="funding_rate", ascending=True)
#         .reset_index(drop=True)
#     )
# 
#     # -----------------------------------
#     # Display results
#     # -----------------------------------
#     st.success("Data fetched successfully!")
# 
#     col1, col2 = st.columns(2)
# 
#     with col1:
#         st.subheader("🟢 Positive Funding Rates (Highest First)")
#         st.write(f"Total: {len(df_positive)}")
#         st.dataframe(df_positive, use_container_width=True)
# 
#     with col2:
#         st.subheader("🔴 Negative Funding Rates (Most Negative First)")
#         st.write(f"Total: {len(df_negative)}")
#         st.dataframe(df_negative, use_container_width=True)
# 
# else:
#     st.info("Click **Fetch Funding Rates** to load live data.")

import streamlit as st

st.set_page_config(layout="centered")

st.title("🚀 We've Moved!")

st.markdown("## This app is now available on our new platform")

st.link_button("👉 Open New Site", "https://aysm.in/fundings")

# st.markdown("### Redirecting you in 3 seconds...")

# st.markdown(
#     """
#     <script>
#         setTimeout(function() {
#             window.open("https://aysm.in/fundings", "_blank");
#         }, 3000);
#     </script>
#     """,
#     unsafe_allow_html=True
# )