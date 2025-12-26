import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Pakistan Property Market Analysis",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #1f77b4;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="main-header">🏠 Pakistan Property Market Analysis</h1>', unsafe_allow_html=True)
st.markdown("""
This dashboard provides insights into the Pakistani property market based on data from Zameen.com.
Explore property trends, prices, and distributions across different cities and property types.
""")

# Load data with all transformations from the notebook
@st.cache_data
def load_data(file_path='Property.csv'):
    # Load the actual dataset
    try:
        df = pd.read_csv(file_path, sep=';')
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found. Please ensure the file is present.")
        return pd.DataFrame()
    
    # Data cleaning and selection steps from the notebook
    df['agency'] = df['agency'].fillna('Unknown')
    df['agent'] = df['agent'].fillna('Unknown')
    
    # Select relevant columns (as in the notebook)
    relevant_columns = [
        'property_type', 'price', 'location', 'city', 'province_name', 
        'latitude', 'longitude', 'baths', 'bedrooms', 'date_added', 
        'area', 'purpose', 'agency', 'agent'
    ]
    df_cleaned = df[relevant_columns].copy()
    
    # Area transformation (as in the notebook)
    df_cleaned['area_value'] = df_cleaned['area'].str.extract(r'(\d+(\.\d+)?)', expand=False)[0].astype(float)
    df_cleaned['area_unit'] = df_cleaned['area'].str.extract(r'([Kk]anal|[Mm]arla)', expand=False)
    df_cleaned['area_unit'] = df_cleaned['area_unit'].str.lower()
    
    df_cleaned['area_in_marla'] = df_cleaned.apply(
        lambda row: row['area_value'] * 20 if row['area_unit'] == 'kanal' else row['area_value'],
        axis=1
    )
    
    # Select final columns (as in the notebook)
    cleaned_columns = [
        'property_type', 'price', 'location', 'city', 'province_name',
        'latitude', 'longitude', 'baths', 'bedrooms', 'date_added',
        'purpose', 'agency', 'agent', 'area_in_marla'
    ]
    
    final_df = df_cleaned[cleaned_columns].copy()
    
    # Convert date_added to datetime and extract year
    final_df['date_added'] = pd.to_datetime(final_df['date_added'], errors='coerce', format='%m-%d-%Y')
    final_df['year_added'] = final_df['date_added'].dt.year
    final_df['month_added'] = final_df['date_added'].dt.month
    
    # Basic outlier removal for visual cleanliness (mimicking notebook analysis)
    final_df = final_df[
        (final_df['baths'] < 100) & 
        (final_df['bedrooms'] < 20) & 
        (final_df['price'] > 1000) & 
        (final_df['year_added'].isin([2018, 2019]))
    ]
    
    return final_df

# Load the data
try:
    df = load_data()
    st.sidebar.success("✅ Data loaded successfully!")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# --- 3. Sidebar and Filtering ---

st.sidebar.header("Filters")

# --- FIXED Q1/Q10 THRESHOLD (Scalar) ---
# This value is used for Q1 and Q10 analysis ONLY.
Q1_HIGH_VALUE_THRESHOLD = 50000000 
st.sidebar.markdown(f"**Q1/Q10 High-Value Threshold:** PKR {Q1_HIGH_VALUE_THRESHOLD:,.0f}")

# Price range filter (Tuple)
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range_tuple = st.sidebar.slider(
    "Price Range (Overall Filter)",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# City filter
cities = sorted(list(df['city'].unique()))
selected_cities = st.sidebar.multiselect(
    'Select Cities for Comparison',
    options=cities,
    default=cities
)

# Property type filter
property_types = sorted(list(df['property_type'].unique()))
selected_property_type = st.sidebar.selectbox("Select Property Type", ['All'] + property_types)

# Purpose filter
purposes = sorted(list(df['purpose'].unique()))
selected_purpose = st.sidebar.selectbox("Select Purpose", ['All'] + purposes)

# Area range filter (Marla)
min_area, max_area = int(df['area_in_marla'].min()), int(df['area_in_marla'].max())
area_range = st.sidebar.slider(
    "Area Range (Marla)",
    min_value=min_area,
    max_value=max_area,
    value=(min_area, max_area)
)

# --- APPLY FILTERS TO CREATE filtered_df ---
filtered_df = df.copy()

if selected_cities:
    filtered_df = filtered_df[filtered_df['city'].isin(selected_cities)]

if selected_property_type != 'All':
    filtered_df = filtered_df[filtered_df['property_type'] == selected_property_type]

if selected_purpose != 'All':
    filtered_df = filtered_df[filtered_df['purpose'] == selected_purpose]

# Apply the price and area range tuples
filtered_df = filtered_df[
    (filtered_df['price'] >= price_range_tuple[0]) &  
    (filtered_df['price'] <= price_range_tuple[1]) &
    (filtered_df['area_in_marla'] >= area_range[0]) & 
    (filtered_df['area_in_marla'] <= area_range[1])
]

# --- 4. Dashboard Content ---

# Display key metrics
st.markdown('<h2 class="section-header">📊 Key Metrics</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Properties", len(filtered_df))

with col2:
    avg_price = filtered_df['price'].mean() if not filtered_df.empty else 0
    st.metric("Average Price", f"₹{avg_price:,.0f}")

with col3:
    avg_area = filtered_df['area_in_marla'].mean() if not filtered_df.empty else 0
    st.metric("Average Area (Marla)", f"{avg_area:.1f}")

with col4:
    most_common_city = filtered_df['city'].mode()[0] if len(filtered_df) > 0 else "N/A"
    st.metric("Most Common City", most_common_city)

st.markdown("---")


# Data Table
st.markdown('<h2 class="section-header">📋 Property Data</h2>', unsafe_allow_html=True)

# Show a sample of the data
if not filtered_df.empty:
    st.dataframe(filtered_df.head(100), use_container_width=True)

    # Download button for filtered data
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_property_data.csv",
        mime="text/csv"
    )
    
    # Show data summary
    with st.expander("📊 Data Summary"):
        st.write("**Dataset Overview:**")
        st.write(f"- Total properties in dataset: {len(df)}")
        st.write(f"- Date range: {df['date_added'].min().strftime('%Y-%m-%d')} to {df['date_added'].max().strftime('%Y-%m-%d')}")
        st.write(f"- Cities covered: {', '.join(sorted(df['city'].unique()))}")
        st.write(f"- Property types: {', '.join(sorted(df['property_type'].unique()))}")
        
        st.write("**Price Statistics:**")
        st.write(f"- Minimum price: {df['price'].min():,}")
        st.write(f"- Maximum price: {df['price'].max():,}")
        st.write(f"- Average price: {df['price'].mean():,.0f}")
        
else:
    st.info("No data available for the selected filters")


# --- Q9: Property Distribution (Sale vs Rent) ---
st.markdown('<h2 class="section-header">Distribution of Property Purposes</h2>', unsafe_allow_html=True)

if not filtered_df.empty:
    purpose_distribution = filtered_df.groupby(['city', 'purpose']).size().reset_index(name='count')
    
    fig_q9 = px.bar(
        purpose_distribution, 
        x='city', 
        y='count', 
        color='purpose',
        title='Sale vs. Rent Listings by City'
    )
    st.plotly_chart(fig_q9, use_container_width=True)
    st.caption("Most listings are typically 'For Sale'.")
else:
    st.info("No data available for the selected filters.")

st.markdown("---")


# --- Price Analysis Section ---
st.markdown('<h2 class="section-header">💰 Price Analysis & Distribution</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Average price by city
    if not filtered_df.empty:
        avg_price_by_city = filtered_df.groupby('city')['price'].mean().sort_values(ascending=False)
        fig3 = px.bar(
            x=avg_price_by_city.index,
            y=avg_price_by_city.values,
            title="Average Price by City",
            labels={'x': 'City', 'y': 'Average Price'},
            color=avg_price_by_city.index
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No data available for the selected filters")

with col2:
    # Average price by property type
    if not filtered_df.empty:
        avg_price_by_type = filtered_df.groupby('property_type')['price'].mean().sort_values(ascending=False)
        fig4 = px.bar(
            x=avg_price_by_type.index,
            y=avg_price_by_type.values,
            title="Average Price by Property Type",
            labels={'x': 'Property Type', 'y': 'Average Price'},
            color=avg_price_by_type.index
        )
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No data available for the selected filters")


# --- 5. Detailed Business Insights (Q1, Q3-Q8, Q10) ---

st.markdown('<h2 class="section-header">📈 Detailed Business Insights</h2>', unsafe_allow_html=True)

# Helper function to compute Top N listings (for Q4, Q10)
def get_top_n_listings(df, group_col, n=10):
    listing_counts = df.groupby([group_col, 'city']).size().reset_index(name='listing_count')
    listing_counts = listing_counts[listing_counts[group_col] != 'Unknown']
    top_n_groups = listing_counts.groupby(group_col)['listing_count'].sum().nlargest(n).index
    return listing_counts[listing_counts[group_col].isin(top_n_groups)]

# Row 1: Q1 and Q5
col_q1, col_q5 = st.columns(2)

with col_q1:
    st.subheader("High-Value Property Growth (YoY)")
    # Use the static Q1_HIGH_VALUE_THRESHOLD here
    high_value_data = df[df['price'] > Q1_HIGH_VALUE_THRESHOLD]
    high_value_growth = high_value_data.groupby(['city', 'year_added']).size().reset_index(name='property_count')
    
    if not high_value_growth.empty and len(high_value_growth['year_added'].unique()) > 1:
        high_value_growth['growth'] = high_value_growth.groupby('city')['property_count'].diff()
        
        fig_q1 = px.line(
            high_value_growth.dropna(), 
            x='year_added', 
            y='property_count', 
            color='city',
            markers=True,
            title=f'Q1: High-Value Listings (> {Q1_HIGH_VALUE_THRESHOLD:,.0f} PKR) Growth'
        )
        fig_q1.update_layout(xaxis={'tickmode': 'linear', 'dtick': 1})
        st.plotly_chart(fig_q1, use_container_width=True)
        st.caption("Tracks the change in luxury property listings year-over-year.")
    else:
        st.info("Q1: Insufficient data for YoY high-value growth analysis.")

with col_q5:
    st.subheader("Seasonal Trend in Property Listings")
    seasonal_trend = filtered_df.groupby(['year_added', 'month_added']).size().reset_index(name='listing_count')
    
    fig_q5 = px.line(
        seasonal_trend, 
        x='month_added', 
        y='listing_count', 
        color='year_added',
        markers=True,
        title='Q5: Seasonal Trend by Month (2018-2019)'
    )
    fig_q5.update_layout(xaxis={'tickmode': 'linear', 'dtick': 1})
    st.plotly_chart(fig_q5, use_container_width=True)
    st.caption("Listing volume usually dips in mid-year (June/July).")

# Row 2: Q7 and Q6
col_q7, col_q6 = st.columns(2)

with col_q7:
    st.subheader("Property Type Prevalence by Province")
    province_property_distribution = df.groupby(['province_name', 'property_type']).size().reset_index(name='count')
    
    fig_q7 = px.bar(
        province_property_distribution, 
        x='province_name', 
        y='count', 
        color='property_type',
        title='Q7: Property Type Prevalence by Province'
    )
    st.plotly_chart(fig_q7, use_container_width=True)
    st.caption("Houses dominate Punjab, while Flats are more prevalent in Sindh.")

with col_q6:
    st.subheader("Area-Price Correlation Table")
    
    correlation_df = filtered_df.groupby(['city', 'property_type']).apply(
        lambda df: df['area_in_marla'].corr(df['price'])
    ).reset_index(name='correlation')

    correlation_df['correlation_strength'] = correlation_df['correlation'].apply(
        lambda x: 'Highly Correlated' if abs(x) >= 0.5 else 'Less Correlated'
    )
    
    st.dataframe(correlation_df.sort_values('correlation', ascending=False).fillna('N/A'))
    st.caption("""
        **Insight:** Area is **highly correlated** (>= 0.5) with price for larger properties, but generally weak for Flats/Portions.
    """)

# Row 3: Q8 and Q3
col_q8, col_q3 = st.columns(2)

with col_q8:
    st.subheader("Influence of Number of Bathrooms on Price")
    df_baths_filtered_q8 = filtered_df[filtered_df['baths'] < 16]
    bathroom_price_influence = df_baths_filtered_q8.groupby(['city', 'baths'])['price'].mean().reset_index()

    fig_q8 = px.line(
        bathroom_price_influence, 
        x='baths', 
        y='price', 
        color='city',
        markers=True,
        title='Q8: Average Price vs. Number of Bathrooms'
    )
    st.plotly_chart(fig_q8, use_container_width=True)
    st.caption("Price generally increases with the number of bathrooms.")

with col_q3:
    st.subheader("Price vs. Bedrooms across Types")
    price_bedroom_variation = filtered_df[filtered_df['bedrooms'] < 15].groupby(['city', 'property_type', 'bedrooms'])['price'].mean().reset_index()
    
    fig_q3 = px.line(
        price_bedroom_variation,
        x='bedrooms',
        y='price',
        color='property_type',
        line_dash='city',
        title='Q3: Avg Price vs. Bedrooms'
    )
    st.plotly_chart(fig_q3, use_container_width=True)
    st.caption("Larger property types see higher prices with more bedrooms; others plateau.")

# Row 4: Q4 and Q10 
col_q4, col_q10 = st.columns(2)

with col_q4:
    st.subheader("Top Agencies (High-Demand Areas)")
    high_demand_areas = df[df['city'].isin(['Karachi', 'Lahore', 'Rawalpindi', 'Islamabad', 'Faisalabad'])]
    agency_listings_top_n = get_top_n_listings(high_demand_areas, 'agency', 10)
    
    if not agency_listings_top_n.empty:
        fig_q4 = px.bar(
            agency_listings_top_n.sort_values(by=['listing_count'], ascending=False), 
            x='listing_count', 
            y='agency', 
            color='city',
            orientation='h',
            title='Q4: Top 10 Agencies by Total Listings',
            height=400
        )
        st.plotly_chart(fig_q4, use_container_width=True)
        st.caption("Activity is heavily concentrated in major metropolitan centers.")
    else:
        st.info("Q4: No agency data available for the analysis.")


with col_q10:
    st.subheader("Top Agents in High-Value Markets")
    # Use the static Q1_HIGH_VALUE_THRESHOLD here
    high_value_data_q10 = filtered_df[filtered_df['price'] > Q1_HIGH_VALUE_THRESHOLD]
    active_agents_top_n = get_top_n_listings(high_value_data_q10, 'agent', 10)
    
    if not active_agents_top_n.empty:
        fig_q10 = px.bar(
            active_agents_top_n.sort_values(by=['listing_count'], ascending=False), 
            x='listing_count', 
            y='agent', 
            color='city',
            orientation='h',
            title=f'Q10: Top 10 Agents in High-Value Markets (> {Q1_HIGH_VALUE_THRESHOLD:,.0f} PKR)',
            height=400
        )
        st.plotly_chart(fig_q10, use_container_width=True)
        st.caption("Agent activity is sensitive to the selected price threshold.")
    else:
        st.warning(f"Q10: No high-value agent listings found above the current threshold.")


# Location Analysis
st.markdown('<h2 class="section-header">🗺️ Location Analysis</h2>', unsafe_allow_html=True)

# Create a map visualization
if not filtered_df.empty:
    center_lat = filtered_df['latitude'].mean() if not filtered_df['latitude'].empty else 30.3753
    center_lon = filtered_df['longitude'].mean() if not filtered_df['longitude'].empty else 69.3451
    
    fig_map = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="price",
        size="area_in_marla",
        hover_name="property_type",
        hover_data=["city", "location", "price", "area_in_marla", "baths", "bedrooms"],
        title="Property Locations in Pakistan",
        zoom=5,
        height=500,
        color_continuous_scale=px.colors.cyclical.IceFire
    )
    
    fig_map.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=center_lat, lon=center_lon),
            zoom=5
        ),
        margin={"r":0,"t":30,"l":0,"b":0}
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Show city statistics
    st.subheader("City-wise Property Distribution")
    city_stats = filtered_df.groupby('city').agg({
        'price': ['count', 'mean', 'median'],
        'area_in_marla': 'mean'
    }).round(2)
    
    city_stats.columns = ['Property Count', 'Avg Price', 'Median Price', 'Avg Area (Marla)']
    st.dataframe(city_stats.sort_values('Property Count', ascending=False))
    
else:
    st.info("No data available for the selected filters to display on the map.")



# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Property Market Analysis Dashboard | Created with Streamlit</p>
        <p><small>Data Source: Zameen.com Property Listings</small></p>
    </div>
    """,
    unsafe_allow_html=True
)