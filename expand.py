import sys,time,argparse,logging
import requests
    

parser = argparse.ArgumentParser()
parser.add_argument("--Surl",help="short url",required=True,dest="url")
args = parser.parse_args()
    
url = args.url

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s",
    level=logging.INFO)


if args.url:
    logging.info(f"CONNECTING to {url}...")
    request = f"https://unshorten.me/raw/{url}"
    response = requests.get(request).text
    logging.info("CONNECTED");time.sleep(1)
    logging.info(f"RESOLVING {url}..");time.sleep(2)
    logging.info("RESOLVED\n");time.sleep(1)
    sys.stdout.write(response)