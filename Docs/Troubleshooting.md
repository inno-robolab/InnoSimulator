<h1 align="center">Troubleshooting</h1>

### Issues that could happen
There're some issues:
1. Localization issue caused by separator signs (`.` and `,` ) on ROS side. In case of using a system localization other than english, this issue could occur.
The error looks like:
```
Received message without an op. All messages require 'op' field with value one of....
```
To fix it change localization to english and check separator signs (it has to be dot sign `.`) in system's properties.

2. Unix epoch time issue. By default it's `System.DateTime(1970, 1, 1, 0, 0, 0, System.DateTimeKind.Utc)` but it has to start from 6th of January and should be look like `System.DateTime(1970, 6, 1, 0, 0, 0, System.DateTimeKind.Utc)`.


