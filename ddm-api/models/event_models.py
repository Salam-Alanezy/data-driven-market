from flask_restx import fields

eventModel = {
    'Date': fields.String(required=True, description='Dato for event/holiday (dd-mm).'),
    'Event/Holiday': fields.String(required=True, description='Navnet på eventet/holidayen.'),
    'Description': fields.String(required=True, description='Beskrivelse av eventet/holidayen.'),
    'FocusGroup': fields.String(required=True, description='Målgruppen for eventet/holidayen.'),
    'TypicalGoodsinHighDemand': fields.String(required=True, description='Typiske varer med høy etterspørsel i forbindelse med eventet/holidayen.'),
    'DigitalMarketingExamples': fields.String(required=True, description='Eksempler på digital markedsføring for eventet/holidayen.'),
    'MarketingLocation': fields.String(required=True, description='Markedsføringssted for eventet/holidayen.'),
    'PreparationTips': fields.String(required=True, description='Forberedelsestips for eventet/holidayen.'),
    'MarketingStartDate': fields.String(required=True, description='Startdato for markedsføring av eventet/holidayen (dd-mm).'),
    'MarketingEndDate': fields.String(required=True, description='Sluttdato for markedsføring av eventet/holidayen (dd-mm).'),
    'EstimatedBudget': fields.String(required=True, description='Estimert budsjett for eventet/holidayen.'),
    'image': fields.String(required=True, description='Bilde')
    
}

getEventModel = {
    'id': fields.String(required=True, description='Eventets ID.'),
    'Date': fields.String(required=True, description='Dato for event/holiday (dd-mm).'),
    'Event/Holiday': fields.String(required=True, description='Navnet på eventet/holidayen.'),
    'Description': fields.String(required=True, description='Beskrivelse av eventet/holidayen.'),
    'FocusGroup': fields.String(required=True, description='Målgruppen for eventet/holidayen.'),
    'TypicalGoodsinHighDemand': fields.String(required=True, description='Typiske varer med høy etterspørsel i forbindelse med eventet/holidayen.'),
    'DigitalMarketingExamples': fields.String(required=True, description='Eksempler på digital markedsføring for eventet/holidayen.'),
    'MarketingLocation': fields.String(required=True, description='Markedsføringssted for eventet/holidayen.'),
    'PreparationTips': fields.String(required=True, description='Forberedelsestips for eventet/holidayen.'),
    'MarketingStartDate': fields.String(required=True, description='Startdato for markedsføring av eventet/holidayen (dd-mm).'),
    'MarketingEndDate': fields.String(required=True, description='Sluttdato for markedsføring av eventet/holidayen (dd-mm).'),
    'EstimatedBudget': fields.String(required=True, description='Estimert budsjett for eventet/holidayen.'),
    'uid': fields.String(required=True, description='Bruker-ID som eier eventet/holidayen.'),
    'createdAt': fields.String(required=True, description='Datoen og tiden da eventet/holidayen ble opprettet.'),
    'image': fields.String(required=True, description='Bilde')
}