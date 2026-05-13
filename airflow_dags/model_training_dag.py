from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def train_churn_model():
    print("Training Random Forest model on cleaned_user_features...")
    # Model training logic would go here

with DAG('churn_prediction_model', start_date=datetime(2026, 1, 1), schedule_interval='@daily') as dag:
    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_churn_model
    )
