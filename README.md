# LIVE_WEATHER_ANALYTICSS
I built an end-to-end data pipeline that:  Collects live weather data via OpenWeatherMap API every 30 minutes , Processes and stores 10+ metrics automatically using Python , Visualizes insights through interactive Power BI dashboards


This project demonstrates end-to-end data engineering and analytics skills by:

Collecting real-time weather data via REST API
Processing and storing data in structured CSV format
Visualizing insights through interactive Power BI dashboards
Monitoring weather patterns and trends over time

The system automatically fetches weather metrics every 30 minutes and maintains a historical dataset for trend analysis.

Data Collection

✅ Automated API calls to OpenWeatherMap
✅ Continuous data collection with configurable intervals
✅ Error handling and logging mechanisms
✅ Structured data storage in CSV format

Metrics Tracked

🌡️ Temperature (Current & Feels Like)
💧 Humidity levels
🌬️ Wind speed
☁️ Cloudiness percentage
🔽 Atmospheric pressure
🌦️ Weather conditions & descriptions

Visualization Dashboard

📊 Multi-page Power BI dashboard with 12+ visualizations
📈 Time-series analysis of weather patterns
🗺️ Geographic location mapping
🔄 Real-time data refresh capabilities
📱 Interactive filters and drill-through features

┌─────────────────┐
│ OpenWeatherMap  │
│      API        │
└────────┬────────┘
         │ REST API Call (Every 30 min)
         ▼
┌─────────────────┐
│  Python Script  │
│  - fetch_data() │
│  - process()    │
│  - save_to_csv()│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CSV Database   │
│ Historical Data │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Power BI      │
│   Dashboard     │
│  (12 Pages)     │
└─────────────────┘
