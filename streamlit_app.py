import streamlit as st
from snowflake.snowpark.context import get_active_session


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Food Delivery Time Predictor",
    page_icon="🍔",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    .prediction-box {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #dddddd;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .prediction-value {
        font-size: 48px;
        font-weight: 700;
    }

    .prediction-label {
        font-size: 18px;
        color: #666666;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SNOWFLAKE CONNECTION
# ============================================================

session = get_active_session()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🍔 Food Delivery Time Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Predict the estimated food delivery time using a Random Forest
    machine learning model deployed in Snowflake.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL INFORMATION
# ============================================================

with st.expander("🤖 Model Information", expanded=False):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Model", "Random Forest")

    with col2:
        st.metric("Model Version", "V2")

    with col3:
        st.metric("MAE", "3.20 min")

    with col4:
        st.metric("R²", "0.8160")

    st.write(
        "The model was trained using 36,394 delivery records and "
        "evaluated on 9,199 test records."
    )

    st.caption(
        "Inference is performed directly through the Snowflake Model Registry "
        "Warehouse-ready model."
    )


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📋 Delivery Information</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the delivery details below and click **Predict Delivery Time**."
)


# ============================================================
# ROW 1 — DELIVERY PERSON
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    delivery_person_age = st.number_input(
        "👤 Delivery Person Age",
        min_value=18,
        max_value=60,
        value=30,
        step=1
    )

with col2:
    delivery_person_ratings = st.number_input(
        "⭐ Delivery Person Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.8,
        step=0.1,
        format="%.1f"
    )

with col3:
    vehicle_condition = st.selectbox(
        "🚗 Vehicle Condition",
        options=[0, 1, 2, 3],
        index=2
    )


# ============================================================
# ROW 2 — LOCATION
# ============================================================

st.markdown(
    '<div class="section-title">📍 Location Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    restaurant_latitude = st.number_input(
        "Restaurant Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=12.9716,
        format="%.6f"
    )

    restaurant_longitude = st.number_input(
        "Restaurant Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=77.5946,
        format="%.6f"
    )

with col2:

    delivery_location_latitude = st.number_input(
        "Delivery Location Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=12.9352,
        format="%.6f"
    )

    delivery_location_longitude = st.number_input(
        "Delivery Location Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=77.6245,
        format="%.6f"
    )


distance_km = st.number_input(
    "📏 Delivery Distance (km)",
    min_value=0.0,
    max_value=50.0,
    value=4.2,
    step=0.1,
    format="%.1f"
)


# ============================================================
# ROW 3 — ORDER INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🕐 Order Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    order_hour = st.slider(
        "Order Hour",
        min_value=0,
        max_value=23,
        value=19,
        step=1
    )

    st.caption(f"Selected time: {order_hour:02d}:00")


with col2:

    pickup_delay_min = st.number_input(
        "Pickup Delay (minutes)",
        min_value=0,
        max_value=60,
        value=10,
        step=1
    )


with col3:

    multiple_deliveries = st.selectbox(
        "Multiple Deliveries",
        options=[0, 1, 2, 3],
        index=1
    )


# ============================================================
# ROW 4 — CONDITIONS
# ============================================================

st.markdown(
    '<div class="section-title">🌦️ Delivery Conditions</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    weather_conditions = st.selectbox(
        "Weather Conditions",
        options=[
            "conditions Sunny",
            "conditions Stormy",
            "conditions Sandstorms",
            "conditions Windy",
            "conditions Cloudy",
            "conditions Fog",
            "conditions Snowy"
        ]
    )

    road_traffic_density = st.selectbox(
        "Road Traffic Density",
        options=[
            "Low",
            "Medium",
            "High",
            "Jam"
        ]
    )


with col2:

    type_of_order = st.selectbox(
        "Type of Order",
        options=[
            "Snack",
            "Meal",
            "Drinks",
            "Buffet"
        ]
    )

    type_of_vehicle = st.selectbox(
        "Type of Vehicle",
        options=[
            "motorcycle",
            "scooter",
            "electric_scooter",
            "bicycle"
        ]
    )


# ============================================================
# ROW 5 — OTHER INFORMATION
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    festival = st.selectbox(
        "🎉 Festival",
        options=[
            "No",
            "Yes"
        ]
    )


with col2:

    city = st.selectbox(
        "🏙️ City",
        options=[
            "Urban",
            "Metropolitian",
            "Semi-Urban"
        ]
    )


with col3:

    st.write("")
    st.write("")
    st.info(
        "The model uses 17 features to estimate delivery time."
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("---")

predict_button = st.button(
    "🚀 Predict Delivery Time",
    type="primary",
    use_container_width=True
)


# ============================================================
# MODEL PREDICTION
# ============================================================

if predict_button:

    with st.spinner("Running Snowflake ML model..."):

        try:

            # ------------------------------------------------
            # Build SQL query
            # ------------------------------------------------

            query = f"""
            SELECT
                (
                    MODEL(
                        FOOD_DELIVERY_ML.ML.FOOD_DELIVERY_RANDOM_FOREST,
                        V2
                    )!PREDICT(
                        {int(delivery_person_age)},
                        {float(delivery_person_ratings)},
                        {float(restaurant_latitude)},
                        {float(restaurant_longitude)},
                        {float(delivery_location_latitude)},
                        {float(delivery_location_longitude)},
                        {float(distance_km)},
                        {int(order_hour)},
                        {int(pickup_delay_min)},
                        '{weather_conditions.replace("'", "''")}',
                        '{road_traffic_density.replace("'", "''")}',
                        {int(vehicle_condition)},
                        '{type_of_order.replace("'", "''")}',
                        '{type_of_vehicle.replace("'", "''")}',
                        {int(multiple_deliveries)},
                        '{festival.replace("'", "''")}',
                        '{city.replace("'", "''")}'
                    ):output_feature_0::FLOAT
                ) AS PREDICTED_TIME
            """

            # ------------------------------------------------
            # Execute model prediction
            # ------------------------------------------------

            result = session.sql(query).collect()

            predicted_time = float(result[0]["PREDICTED_TIME"])

            predicted_time = round(predicted_time, 2)


            # =================================================
            # DISPLAY RESULT
            # =================================================

            st.markdown(
                f"""
                <div class="prediction-box">
                    <div class="prediction-label">
                        Estimated Delivery Time
                    </div>
                    <div class="prediction-value">
                        {predicted_time:.2f} minutes
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # INTERPRETATION
            # =================================================

            if predicted_time < 20:

                st.success(
                    "🟢 The estimated delivery time is relatively short."
                )

            elif predicted_time < 35:

                st.info(
                    "🟡 The estimated delivery time is moderate."
                )

            else:

                st.warning(
                    "🟠 The estimated delivery time is relatively long."
                )


            # =================================================
            # INPUT SUMMARY
            # =================================================

            st.markdown(
                '<div class="section-title">📊 Prediction Details</div>',
                unsafe_allow_html=True
            )

            summary_col1, summary_col2, summary_col3 = st.columns(3)

            with summary_col1:

                st.metric(
                    "Distance",
                    f"{distance_km:.1f} km"
                )

                st.metric(
                    "Order Time",
                    f"{order_hour:02d}:00"
                )

            with summary_col2:

                st.metric(
                    "Traffic",
                    road_traffic_density
                )

                st.metric(
                    "Weather",
                    weather_conditions.replace(
                        "conditions ",
                        ""
                    )
                )

            with summary_col3:

                st.metric(
                    "Vehicle",
                    type_of_vehicle
                )

                st.metric(
                    "Pickup Delay",
                    f"{pickup_delay_min} min"
                )


            # =================================================
            # MODEL DETAILS
            # =================================================

            with st.expander("🔍 Prediction Technical Details"):

                st.write(
                    "Prediction generated by:"
                )

                st.code(
                    "FOOD_DELIVERY_ML.ML."
                    "FOOD_DELIVERY_RANDOM_FOREST"
                    " — V2"
                )

                st.write(
                    "Inference platform: Snowflake Warehouse"
                )

                st.write(
                    "Model: Random Forest Regressor"
                )

                st.write(
                    "Training rows: 36,394"
                )

                st.write(
                    "Test rows: 9,199"
                )

                st.write(
                    "Mean Absolute Error: 3.20 minutes"
                )

                st.write(
                    "Root Mean Squared Error: 4.05 minutes"
                )

                st.write(
                    "R² Score: 0.8160"
                )


        except Exception as e:

            st.error(
                "Prediction failed."
            )

            st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Food Delivery Time Prediction • "
    "Snowflake ML • Random Forest • Model Registry V2"
)