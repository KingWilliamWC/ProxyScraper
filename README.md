# ProxyScraper
<img src="https://img.shields.io/badge/build-passing-brightgreen"></img>
<img src="https://img.shields.io/badge/python-v3.8-blue"></img>
<img src="https://img.shields.io/badge/files-1-blue"></img>

<br>
A simple proxy scraper from a free API that outputs the results to a text file
<br>
<br>
Requires the requests library
<br>
<a href="https://github.com/psf/requests#installing-requests-and-supported-versions"><img src="https://img.shields.io/badge/requests-latest-brightgreen"></img></a>

# Install
`git clone https://github.com/KingWilliamWC/ProxyScraper.git`
<br>
<br>
`cd ProxyScraper/`

# Usage
for help:
`python proxy-scraper.py -h`
## Set Limit
Sets the limit for the amount of proxies to source
#### Bash:
```console
python3 proxy-scraper.py -limit [1-3000]
```
#### CMD:
```console
python proxy-scraper.py -limit [1-3000]
```
<br>

## Set Proxy Type
Sets the proxy serving type
#### Bash:
```console
python3 proxy-scraper.py -type [http,https,socks4,socks5]
```
#### CMD:
```console
python proxy-scraper.py -type [http,https,socks4,socks5]
```

<br>

## Set Port Type
Sets the port to search for
#### Bash:
```console
python3 proxy-scraper.py -port [x]
```
#### CMD:
```console
python proxy-scraper.py -port [x]
```
<br>

## Set Output File
Sets the file where the results are stored
#### Bash:
```console
python3 proxy-scraper.py -output [output_filename.txt]
```
#### CMD:
```console
python proxy-scraper.py -output [output_filename.txt]
```
