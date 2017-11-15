# stoxfaas 
## A OPENFAAS Serverless function for fetching stock prices

A sample function to demonstrate fetching stock prices from [Yahoo! finance](https://in.finance.yahoo.com/) given a NASDAQ stock symbol.
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
- 

