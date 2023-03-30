# Upload de arquivos individuais para o MinIO
# Implementa barra de progresso

import os
import boto3
import tqdm
from botocore.client import Config

def upload_file_to_s3(session, *, bucket, key, filename):
    file_size = os.stat(filename).st_size
    s3 = session.client('s3',
        endpoint_url='https://one.s3.es.gov.br',
        aws_access_key_id='ACCESS_KEY',
        aws_secret_access_key='SECRET_ACCESS_KEY',
        config=Config(signature_version='s3v4'),
        region_name='sa-east-1'
    )
    with tqdm.tqdm(total=file_size, unit="B", unit_scale=True, desc=filename) as pbar:
        s3.upload_file(
            Filename=filename,
            Bucket=bucket,
            Key=key,
            Callback=lambda bytes_transferred: pbar.update(bytes_transferred),
        )

if __name__ == "__main__":
    
    session = boto3.Session()

    upload_file_to_s3(
        session,
        bucket='BUCKET',
        key='bronze/nome_objeto_no_bucket',
        filename=r'D:\PASTA\NOME_DO_ARQUIVO',
    )