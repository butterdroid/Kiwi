# Generated by Django 2.1.2 on 2018-10-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('testcases', '0002_squashed'),
        ('management', '0001_squashed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestBuild',
            new_name='Build',
        ),
        migrations.RenameModel(
            old_name='TCMSEnvGroup',
            new_name='EnvGroup',
        ),
        migrations.RenameModel(
            old_name='TCMSEnvGroupPropertyMap',
            new_name='EnvGroupPropertyMap',
        ),
        migrations.RenameModel(
            old_name='TCMSEnvProperty',
            new_name='EnvProperty',
        ),
        migrations.RenameModel(
            old_name='TCMSEnvValue',
            new_name='EnvValue',
        ),
        migrations.AlterField(
            model_name='EnvGroup',
            name='property',
            field=models.ManyToManyField(related_name='group',
                                         through='management.EnvGroupPropertyMap',
                                         to='management.EnvProperty'),
        ),
        migrations.AlterField(
            model_name='EnvGroupPropertyMap',
            name='group',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='management.EnvGroup'),
        ),
        migrations.AlterField(
            model_name='EnvGroupPropertyMap',
            name='property',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='management.EnvProperty'),
        ),
        migrations.AlterField(
            model_name='EnvValue',
            name='property',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE,
                                    related_name='value', to='management.EnvProperty'),
        ),
        migrations.RenameModel(
            old_name='TestTag',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='product',
        ),
        migrations.RemoveField(
            model_name='build',
            name='milestone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='default_milestone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='milestone_url',
        ),
        migrations.DeleteModel(
            name='Milestone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='disallow_new',
        ),
        migrations.RemoveField(
            model_name='product',
            name='max_vote_super_bug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vote_super_user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='votes_to_confirm',
        ),
        migrations.AlterModelTable(
            name='build',
            table=None,
        ),
        migrations.AlterModelTable(
            name='classification',
            table=None,
        ),
        migrations.AlterModelTable(
            name='component',
            table=None,
        ),
        migrations.AlterModelTable(
            name='envgroup',
            table=None,
        ),
        migrations.AlterModelTable(
            name='envgrouppropertymap',
            table=None,
        ),
        migrations.AlterModelTable(
            name='envproperty',
            table=None,
        ),
        migrations.AlterModelTable(
            name='envvalue',
            table=None,
        ),
        migrations.AlterModelTable(
            name='priority',
            table=None,
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tag',
            table=None,
        ),
        migrations.AlterModelTable(
            name='version',
            table=None,
        ),
        migrations.RemoveField(
            model_name='envgroup',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='envgroup',
            name='modified_by',
        ),
    ]