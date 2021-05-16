# mcstatus
Simple discord bot that allows you to view info on some servers.

Uses [mcstatus](https://github.com/Dinnerbone/mcstatus).

In order for it to work, server must have query enabled in the server.properties file.

### Common issues:
**Bot times out even though query is active.**

Change the query port to the server port so they are the same.
Make sure your server has the query port open.

### Commands:

Command | Result
------------ | -------------
**!players** | Outputs players online in the server.
**!info** | Displays server info.
