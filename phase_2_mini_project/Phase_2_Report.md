# Order Delay Intelligence: Findings & Recommendations

## Overview
This project focused on analyzing the Brazilian E-Commerce Public Dataset by Olist to predict which orders are likely to be delayed and understand the underlying factors driving these delays.

### Key Metrics
- **Overall Delay Rate**: 7.91% of delivered orders arrived after the estimated delivery date.
- **Top Delayed States**: AL (Alagoas) at 24.12%, MA (Maranhão) at 20.38%, and SE (Sergipe) at 16.27%.
- **Top Delayed Categories**: Audio products (12.71%) and Fashion/Underwear (12.60%).

## Model Performance
We trained several classification models to predict delays. Due to class imbalance, we optimized for the AUC-ROC score and balanced class weights:
- **Logistic Regression AUC**: 0.685
- **Random Forest AUC**: 0.716
- **XGBoost AUC**: 0.731 (Average CV ROC-AUC: 0.7295 +/- 0.0105)

XGBoost provided the best predictive capability, and the 5-fold cross-validation confirmed its stability. While precision for delays is naturally low due to the imbalanced nature of the dataset (many more on-time than delayed deliveries), the model successfully identifies a majority of delayed orders (recall ~57%).

## Delay Magnitude
For orders that miss their estimated delivery date, the delays are significant:
- **Average Delay**: 8.7 days
- **Median Delay**: 5.0 days
- **90th Percentile**: 20.0 days (10% of delayed orders are late by 20+ days).

## Interpretability & Insights (SHAP)
Using SHAP values to interpret the XGBoost model revealed the most important drivers of delay:
1. **Estimated Delivery Days**: Orders with shorter estimated delivery windows are much more prone to being delayed. The logistics network might be systematically over-promising on specific routes.
2. **Freight Ratio (Freight / Price)**: Higher freight costs relative to the item price correlate with delays, potentially indicating long-distance, bulky, or complex shipments.
3. **Product Weight**: Heavier products show higher likelihoods of missing their delivery targets.
4. **Customer State**: Certain states (like AL, MA, RJ) strongly push the model toward predicting a delay.

## Business Recommendations
1. **Recalibrate Delivery Estimates**: For orders heading to Northern/Northeastern states (AL, MA, SE) or involving heavy items, pad the estimated delivery date by 2-3 days to set realistic customer expectations and reduce frustration.
2. **Review Carrier Contracts**: Investigate why high-freight-ratio and heavy items are consistently delayed. Renegotiating SLAs with carriers handling these specific routes or categories could improve performance.
3. **Proactive Customer Support**: Integrate the XGBoost model into the logistics pipeline. If an order is flagged with a high probability of delay at purchase, automatically notify the customer in advance or offer expedited shipping discounts on future orders.
