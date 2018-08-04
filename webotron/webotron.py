import boto3
import click
session = boto3.Session()
s3 = session.resource('s3')


@click.group()
def cli():
    "webtron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"

    for bucket in s3.buckets.all():    
        print(bucket.name)
        
@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):        
    "List objects in a s3 buckets"   
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
        
if __name__== '__main__':  
    cli()