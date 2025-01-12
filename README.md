
import dagshub
dagshub.init(repo_owner='diazmanne', repo_name='MLFlow-Basic-Operation', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)
