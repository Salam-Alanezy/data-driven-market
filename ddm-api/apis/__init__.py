from flask_restx import Api

from .store_products import api as store_prod_api
from .store_layout import api as layout_api
from .storeage import api as storage_api
from .shopping import api as sho_api
from .auth import api as auth_api
from .event import api as event_api
from .categories import api as cat_api
from .priority import api as pri_api
from .strategies import api as str_api
from .geo import api as geo_api
from .company import api as com_api
from .kassal import api as kass_api
from .store_activities import api as act_api
from swagger_doc.global_swagger import title, description, version





api = Api(
    title=title,
    version=version,
    description=description,
    default_mediatype="application/x-www-form-urlencoded"
)

# Data namespace
api.add_namespace(auth_api, path="/v1/auth")
api.add_namespace(store_prod_api, path="/v1/store")
api.add_namespace(cat_api, path="/v1/categories")
api.add_namespace(storage_api, path="/v1/storage")
api.add_namespace(sho_api, path="/v1/shopping")
api.add_namespace(event_api, path="/v1/events")
api.add_namespace(kass_api, path="/v1/kassal")
api.add_namespace(act_api, path="/v1/activities")

# api.add_namespace(pri_api, path="/v1/prio")
# api.add_namespace(str_api, path="/v1/strategy")
# api.add_namespace(geo_api, path="/v1/geo")
# api.add_namespace(com_api, path="/v1/company")

#api.add_namespace(layout_api, path="/v1/strategies")

