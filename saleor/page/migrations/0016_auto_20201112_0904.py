# Generated by Django 3.1 on 2020-11-12 09:04

from django.db import migrations

import saleor.core.db.fields
import saleor.core.sanitizers.editorjs_sanitizer


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0015_migrate_from_draftjs_to_editorjs_format"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content_json",
            field=saleor.core.db.fields.SanitizedJSONField(
                blank=True,
                default=dict,
                sanitizer=saleor.core.sanitizers.editorjs_sanitizer.clean_editor_js,
            ),
        ),
        migrations.AlterField(
            model_name="pagetranslation",
            name="content_json",
            field=saleor.core.db.fields.SanitizedJSONField(
                blank=True,
                default=dict,
                sanitizer=saleor.core.sanitizers.editorjs_sanitizer.clean_editor_js,
            ),
        ),
    ]
