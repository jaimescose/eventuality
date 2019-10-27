import graphene

class EventSubcategoryInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String(required=True)
    description = graphene.String(required=False)

class EventCategoryInput(EventSubcategoryInput):
    parent_category = EventSubcategoryInput(required=False)
