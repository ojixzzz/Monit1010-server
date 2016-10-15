import falcon
import json
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=1)

class DataStatusResource:
    def on_get(self, req, resp):

        monit1010 = mc.get("monit1010")
        if monit1010:
        	monit1010['api4shared_status'] = mc.get("monit1010_4shared")
        	resp.body = json.dumps({"status": 200, "data": monit1010})
        else:
        	resp.body = json.dumps({"status": 404})

api = falcon.API()
api.add_route('/data_status', DataStatusResource())