import  zenoss_api
import json

z=zenoss_api.ZenossAPIExample()
d=json.dumps(z.get_events(),indent=4)
print d
