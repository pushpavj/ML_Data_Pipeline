
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
#cloud api details
API_KEY = "YELNCGKJF3NIGZZ6" #os.getenv('API_KEY',None)
API_SECRET_KEY = "qz5rY/LYqEWzrR2Tr5kXNFgSzKDa5EzwkFhhs8bgfDTAPmYugGKvqIN/ekTc9r95"
#os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092"
#os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)

#Schema related variables
SCHEMA_REGISTRY_API_KEY = "HNR5STLMDDQ65Z2U" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "HGRAiJlUIEAJLAGSEPd1+F3aNfGCEcR7tXeTyYX+vNKmuawJijZDjDUYRfvsn7z2"
#os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
ENDPOINT_SCHEMA_URL  ="https://psrc-10wgj.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)

def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

