# Varre os arquivos de um diretório e faz upload para a AWS usando o Boto3
# Implementa uma barra de progresso para acompanhar o upload

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
    dir_path = r'D:\Backup\RAIS'
    bucket_path = r'bronze/rais/2020/'

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            upload_file_to_s3(
                session,
                bucket='datalake-emerson-edc',
                key=bucket_path+path,
                filename=dir_path+'\\'+path,
            )
