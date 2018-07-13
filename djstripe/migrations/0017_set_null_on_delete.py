# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-05 12:04
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0016_stripe_id_255_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='default_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers',
                                    to='djstripe.StripeSource'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='source',
            field=models.ForeignKey(help_text='The source used for this charge.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='charges',
                                    to='djstripe.StripeSource'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscription',
            field=models.ForeignKey(help_text='The subscription that this invoice was prepared for, if any.',
                                    null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='invoices', to='djstripe.Subscription'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='plan',
            field=models.ForeignKey(
                help_text='If the invoice item is a proration, the plan of the subscription for \
                which the proration was computed.', null=True, on_delete=django.db.models.deletion.SET_NULL,
                related_name='invoiceitems', to='djstripe.Plan'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='subscription',
            field=models.ForeignKey(
                help_text='The subscription that this invoice item has been created for, \
                if any.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoiceitems',
                to='djstripe.Subscription'),
        ),
    ]