import graphene
from graphene_django import DjangoObjectType

class Query(graphene.ObjectType):
    unverified = graphene.String()
    verified = graphene.String(token=graphene.String(required=True))

    def resolve_unverified(root, info):
        return "This is an unverified response!"

    def resolve_verified(root, info, token):
        #at some point, actually verify the token
        return token

schema = graphene.Schema(query=Query)
