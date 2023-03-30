# Upload de arquivos individuais para o AWS com boto3
# Implementa barra de progresso

import os
import boto3
import tqdm

def upload_file_to_s3(session, *, bucket, key, filename):
    file_size = os.stat(filename).st_size
    s3 = session.client("s3")
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
        bucket='datalake-emerson-edc',
        key='bronze/rais/2020/rais_vinc_pub_centro_oeste.txt',
        filename=r'D:\Backup\RAIS\RAIS_VINC_PUB_CENTRO_OESTE.txt',
    )