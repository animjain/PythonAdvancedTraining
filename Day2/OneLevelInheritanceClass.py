if 'drive' in c1.__dict__:
    c1.__class__.get('drive')
elif 'drive' in c1.__class__.__dict__:
    c1.__class__.__dict__.get('drive')(c1)

# notice c1 : if you are calling super class method and you need to call super calss method with base class object,
# then you need to also pass object as first argument.
