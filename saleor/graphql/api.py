import graphene
from graphene_federation.main import _get_query

from .account.schema import AccountMutations, AccountQueries
from .app.schema import AppMutations, AppQueries
from .attribute.schema import AttributeMutations, AttributeQueries
from .channel.schema import ChannelMutations, ChannelQueries
from .checkout.schema import CheckoutMutations, CheckoutQueries
from .core.schema import CoreMutations, CoreQueries
from .csv.schema import CsvMutations, CsvQueries
from .discount.schema import DiscountMutations, DiscountQueries
from .giftcard.schema import GiftCardMutations, GiftCardQueries
from .invoice.schema import InvoiceMutations
from .menu.schema import MenuMutations, MenuQueries
from .meta.schema import MetaMutations
from .order.schema import OrderMutations, OrderQueries
from .page.schema import PageMutations, PageQueries
from .payment.schema import PaymentMutations, PaymentQueries
from .plugins.schema import PluginsMutations, PluginsQueries
from .product.schema import ProductMutations, ProductQueries
from .shipping.schema import ShippingMutations, ShippingQueries
from .shop.schema import ShopMutations, ShopQueries
from .translations.schema import TranslationQueries
from .warehouse.schema import StockQueries, WarehouseMutations, WarehouseQueries
from .webhook.schema import WebhookMutations, WebhookQueries


class Query(
    AccountQueries,
    AppQueries,
    AttributeQueries,
    ChannelQueries,
    CheckoutQueries,
    CoreQueries,
    CsvQueries,
    DiscountQueries,
    PluginsQueries,
    GiftCardQueries,
    MenuQueries,
    OrderQueries,
    PageQueries,
    PaymentQueries,
    ProductQueries,
    ShippingQueries,
    ShopQueries,
    StockQueries,
    TranslationQueries,
    WarehouseQueries,
    WebhookQueries,
):
    pass


class Mutation(
    AccountMutations,
    AppMutations,
    AttributeMutations,
    ChannelMutations,
    CheckoutMutations,
    CoreMutations,
    CsvMutations,
    DiscountMutations,
    PluginsMutations,
    GiftCardMutations,
    InvoiceMutations,
    MenuMutations,
    MetaMutations,
    OrderMutations,
    PageMutations,
    PaymentMutations,
    ProductMutations,
    ShippingMutations,
    ShopMutations,
    WarehouseMutations,
    WebhookMutations,
):
    pass


def fix_implements_separator(fn):
    """Support multiple interface notation in schema for Apollo tooling.

    In `graphql-core` V2 separator for interaces is `,`.
    Apollo tooling to generate TypeScript types using `&` as interfaces separator.
    https://github.com/graphql-python/graphql-core-legacy/pull/258
    https://github.com/graphql-python/graphql-core-legacy/issues/176
    """

    def wrapped(self, *args, **kw):
        original_schema = fn(self, *args, **kw)
        new_schema = ""
        for line in original_schema.splitlines():
            if "implements" in line:
                line = line.replace(",", " &")
            new_schema += f"{line}\n"
        return new_schema

    return wrapped


def build_schema(query=None, mutation=None, **kwargs):
    GrapheneSchema = graphene.Schema
    GrapheneSchema.__str__ = fix_implements_separator(GrapheneSchema.__str__)
    schema = GrapheneSchema(query=query, mutation=mutation, **kwargs)
    return GrapheneSchema(query=_get_query(schema, query), mutation=mutation, **kwargs)


schema = build_schema(Query, mutation=Mutation)
