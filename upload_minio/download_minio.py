# Download de arquivos individuais do MinIO
# Implementa barra de progresso

import boto3
import tqdm
from botocore.client import Config

def download_file_to_s3(ssession, *, bucket, key, version_id=None, filename):
    
    s3 = session.client('s3',
        endpoint_url='https://one.s3.es.gov.br',
        aws_access_key_id='ACCESS-KEY',
        aws_secret_access_key='SECRET-ACCESS-KEY',
        config=Config(signature_version='s3v4'),
        region_name='sa-east-1'
    )

    kwargs = {"Bucket": bucket, "Key": key}

    if version_id is not None:
        kwargs["VersionId"] = version_id
    
    object_size = s3.head_object(**kwargs)["ContentLength"]

    if version_id is not None:
        ExtraArgs = {"VersionId": version_id}
    else:
        ExtraArgs = None
    
    with tqdm.tqdm(total=object_size, unit="B", unit_scale=True, desc=filename) as pbar:
      s3.download_file(
        Bucket=bucket,
        Key=key,
        ExtraArgs=ExtraArgs,
        Filename=filename,
        Callback=lambda bytes_transferred: pbar.update(bytes_transferred),
    )
        
if __name__ == "__main__":
    
    session = boto3.Session()

    download_file_to_s3(
        session,
        bucket='BUCKET',
        key='PASTA/NOME_OBJETO_NO_BUCKET',
        filename=r'D:\PASTA\NOME_ARQUIVO',
    )