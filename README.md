python-bf3stats
===============
Provide a simple Python interface to the [bf3stats.com API](http://bf3stats.com/api)

Where is the documentation?
---------------------------
Maybe I'll add one in the near future.
Feel free to fork this repository and create one. I look forward to pull requests.

Code example?
-------------
```python
import bf3stats
bf3stats = bf3stats.api()
# show count of online players
bf3stats.onlinestats()
```
Should show:
``` {u'360': 18166, u'pc': 38419, u'ps3': 40362, u'status': u'ok'} ```

```python
import bf3stats
bf3stats = bf3stats.api()
# get a dict with short stats of player O2ON
result = bf3stats.player('O2ON')
```
Look in result ;)