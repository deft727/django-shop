from django import template

register= template.Library()

TABLE_HEAD= """
<table class="table table-bordered">
				<tbody>
				
				
"""
TABLE_TEIL="""
                    </tbody>
				</table>
                """
TABLE_CONTENT="""
                <tr class="techSpecRow"><th colspan="2">Product Details</th></tr>
				<tr class="techSpecRow"><td class="techSpecTD1"> {name} </td><td class="techSpecTD2">Задача 2 мл</td></tr>
        		<tr class="techSpecRow"><td class="techSpecTD1"> {value} </td><td class="techSpecTD2">probes</td></tr>
"""

PRODUCT_SPEC={
    'pafume':{

        'volume':'volume',
        'notes':'notes',
        'fragrance_type':'fragrance_type',
        'gender':'gender'

    },
    'probes':{

        'volume':'volume',
        'notes':'notes',
        'fragrance_type':'fragrance_type',
        'gender':'gender'
    }

}

def get_product_spec(product,model_name):
    table_content=''
    for name,value in PRODUCT_SPEC[model_name].items():
        table_content+= TABLE_CONTENT.format(name=name,value=getattr(product,value))
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',table_content)
    return table_content

@register.filter
def product_spec(product):
    model_name=product.__class__._meta.model_name
    return TABLE_HEAD + get_product_spec(product,model_name) + TABLE_TEIL