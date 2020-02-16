# sp20-516-250 E.Cloudmesh.Common.2

from cloudmesh.common.dotdict import dotdict
store = {
"name": "Amazon"
}
store = dotdict(store)
print(store["name"])
