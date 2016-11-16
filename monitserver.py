import falcon
import json
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=1)

class DataStatusResource:
    def on_get(self, req, resp):

        monit1010 = mc.get("monit1010")
        if monit1010:
            data = {
                "chart1_list": monit1010['autodownload_list'],
                "chart2_list": monit1010['link4share_list'],
                "chart3_list": monit1010['apkpoke_list'],
                "data1_label": "AutoDownload<br/> Online:",
                "data2_label": "Link4share<br/> Online:",
                "data3_label": "Apkpoke<br/> Online:",
                "data4_label": "Api 4shared:",
                "data5_label": "Server Status:",
                "data6_label": "Transaksi Laundry<br/>(Today):",
                "data1": monit1010['autodownload_online'],
                "data2": monit1010['link4share_online'],
                "data3": monit1010['apkpoke_online'],
                "data4": mc.get("monit1010_4shared"),
                "data5": monit1010['server_status'],
                "data6": 0,
            }
            resp.body = json.dumps({"status": 200, "data": data})
        else:
            resp.body = json.dumps({"status": 404})

api = falcon.API()
api.add_route('/data_status', DataStatusResource())