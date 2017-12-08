# stoxfaas 
## An OPENFAAS Serverless function for fetching stock prices

A sample function to demonstrate fetching stock prices from [Yahoo! finance](https://finance.yahoo.com/quote/USA/) given a NASDAQ stock symbol.
The functions fetches the current and historical stock prices for the requested symbol for all trading sessions within the last 7 days.

Example:

```
[root@localhost stoxfaas]# curl http://gatewayip:8080/function/stoxfaas -d "IBM"
                  Open        High         Low       Close   Adj Close   Volume
Date
2017-11-08  151.600006  151.789993  150.279999  151.570007  150.070007  4634400
2017-11-09  149.929993  151.800003  149.860001  150.300003  150.300003  4776500
2017-11-10  150.649994  150.889999  149.139999  149.160004  149.160004  4307300
2017-11-13  148.880005  149.000000  147.919998  148.399994  148.399994  5085300
2017-11-14  147.949997  148.970001  147.490005  148.889999  148.889999  3691900
```

## Assumptions ##
- A functional [Openfaas](http://github.com/openfaas/) deployment with [CLI](http://github.com/openfaas/). A quick [Guide](https://blog.alexellis.io/first-faas-python-function/)

## Deploying **stoxfaas** on OPENFAAS

### Getting stoxfaas

``git clone https://github.com/ashrathi/stoxfaas.git``

### Tailor it for your environment

#### Gateway
The code assumes the openfaas API gateway to be http://localhost:8080.  <br>
You can change this to required values in by updating the `gateway` value `stoxfaas.yml`

#### Docker Image Name
For multi-node deployments, update the `image` name in `stoxfaas.yml` to point to appropriate private registry or docker hub repositories

### Building stoxfaas

````
cd stoxfaas
faas-cli build -f stack.yml
faas-cli push -f stack.yml
faas-cli deploy -f stack.yml
````

After deployment, it may take a few minutes for the service to be available depending on the amount of time it takes for the docker image download. Please be patient!

### Testing stoxfaas

````
curl http://gatewayip:8080/function/stoxfaas -d "IBM"
curl http://gatewayip:8080/function/stoxfaas -d "AAPL"
curl http://gatewayip:8080/function/stoxfaas -d "GOOG"
````

## Maintainer ##

**Ashish Rathi** <br>
*Senior Architect* <br>
[Accelerite](https://accelerite.com/) <br>

<img src="https://pbs.twimg.com/profile_images/448567753041907712/Kg-Vptrq_400x400.png" width="48">

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40ashrathi)](https://twitter.com/ashrathi) <br>
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40accelerite)](https://twitter.com/accelerite)
