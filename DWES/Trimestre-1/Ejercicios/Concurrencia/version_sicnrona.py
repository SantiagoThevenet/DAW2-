import requests
import time


def download_site(url, s):
    with s.get(url) as response:
        print("Read {} from {}".format(len(response.content), url))


def download_all_sites(sites):
    with requests.Session() as s:
        for url in sites:
            download_site(url, s)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print("Downloaded {} sites in {} seconds".format(len(sites), duration))

