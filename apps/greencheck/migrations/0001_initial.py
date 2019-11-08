# Generated by Django 2.2.6 on 2019-11-01 08:35

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('accounts', '0002_add_django_user_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='GreencheckIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(null=True)),
                ('ip_end', models.IntegerField(db_column='ip_eind')),
                ('ip_start', models.IntegerField()),
                ('hostingprovider', models.ForeignKey(db_column='id_hp', on_delete=django.db.models.deletion.CASCADE, to='accounts.Hostingprovider')),
            ],
            options={
                'db_table': 'greencheck_ip',
            },
        ),
        migrations.CreateModel(
            name='Greencheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_unixdatetimefield.fields.UnixDateTimeField(db_column='datum')),
                ('green', django_mysql.models.EnumField(choices=[('yes', 'yes'), ('no', 'no'), ('old', 'old')])),
                ('ip', models.IntegerField()),
                ('tld', models.CharField(max_length=64)),
                ('type', django_mysql.models.EnumField(choices=[('as', 'asn'), ('ip', 'ip'), ('none', 'none'), ('url', 'url'), ('whois', 'whois')])),
                ('url', models.CharField(max_length=255)),
                ('greencheck_ip', models.ForeignKey(db_column='id_greencheck', default=0, on_delete=django.db.models.deletion.CASCADE, to='greencheck.GreencheckIp'))
            ],
            options={
                'db_table': 'greencheck',
            },
        ),
        migrations.CreateModel(
            name='GreencheckASN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(null=True)),
                ('asn', models.IntegerField(verbose_name='Autonomous system number')),
                ('hostingprovider', models.ForeignKey(db_column='id_hp', on_delete=django.db.models.deletion.CASCADE, to='accounts.Hostingprovider'))
            ],
            options={
                'db_table': 'greencheck_as',
            },
        ),
        migrations.CreateModel(
            name='GreencheckASNapprove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField()),
                ('asn', models.IntegerField()),
                ('status', models.TextField()),
                ('hostingprovider', models.ForeignKey(db_column='id_hp', on_delete=django.db.models.deletion.CASCADE, to='accounts.Hostingprovider')),
                ('greencheck_asn', models.ForeignKey(db_column='idorig', on_delete=django.db.models.deletion.CASCADE, to='greencheck.GreencheckASN'))
            ],
            options={
                'db_table': 'greencheck_as_approve',
            },
        ),
        migrations.CreateModel(
            name='GreencheckIpApprove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField()),
                ('ip_end', models.IntegerField(db_column='ip_eind')),
                ('ip_start', models.IntegerField()),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'greencheck_ip_approve',
            },
        ),
        migrations.CreateModel(
            name='GreencheckLinked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GreencheckStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_through', django_mysql.models.EnumField(choices=[('admin', 'admin'), ('api', 'api'), ('apisearch', 'apisearch'), ('bots', 'bots'), ('test', 'test'), ('website', 'website')])),
                ('count', models.IntegerField()),
                ('ips', models.IntegerField()),
            ],
            options={
                'db_table': 'greencheck_stats',
            },
        ),
        migrations.CreateModel(
            name='GreencheckStatsTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_through', django_mysql.models.EnumField(choices=[('admin', 'admin'), ('api', 'api'), ('apisearch', 'apisearch'), ('bots', 'bots'), ('test', 'test'), ('website', 'website')])),
                ('count', models.IntegerField()),
                ('ips', models.IntegerField()),
            ],
            options={
                'db_table': 'greencheck_stats_total',
            },
        ),
        migrations.CreateModel(
            name='GreencheckTLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_domains', models.IntegerField()),
                ('green_domains', models.IntegerField()),
                ('hps', models.IntegerField()),
                ('tld', models.CharField(max_length=50)),
                ('toplevel', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'greencheck_tld',
            },
        ),
        migrations.CreateModel(
            name='GreencheckWeeklyStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checks_green', models.IntegerField()),
                ('checks_grey', models.IntegerField()),
                ('checks_perc', models.FloatField()),
                ('checks_total', models.IntegerField()),
                ('monday', models.DateField(db_column='maandag')),
                ('url_green', models.IntegerField()),
                ('url_grey', models.IntegerField()),
                ('url_perc', models.FloatField()),
                ('week', models.IntegerField()),
                ('year', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'greencheck_weekly',
            },
        ),
        migrations.CreateModel(
            name='GreenList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_checked', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('name', models.CharField(db_column='naam', max_length=255)),
                ('type', django_mysql.models.EnumField(choices=[('as', 'asn'), ('ip', 'ip'), ('none', 'none'), ('url', 'url'), ('whois', 'whois')])),
                ('url', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('greencheck', models.ForeignKey(db_column='id_greencheck', on_delete=django.db.models.deletion.CASCADE, to='greencheck.Greencheck')),
                ('hostingprovider', models.ForeignKey(db_column='id_hp', on_delete=django.db.models.deletion.CASCADE, to='accounts.Hostingprovider')),
            ],
            options={
                'db_table': 'greenlist',
            },
        ),
        migrations.AddIndex(
            model_name='greenchecktld',
            index=models.Index(fields=['tld'], name='tld'),
        ),
        migrations.AddIndex(
            model_name='greencheckstatstotal',
            index=models.Index(fields=['checked_through'], name='checked_through'),
        ),
        migrations.AddIndex(
            model_name='greencheckstats',
            index=models.Index(fields=['checked_through'], name='checked_through'),
        ),
        migrations.AddField(
            model_name='greencheckipapprove',
            name='greencheck_ip',
            field=models.ForeignKey(db_column='idorig', on_delete=django.db.models.deletion.CASCADE, to='greencheck.GreencheckIp'),
        ),
        migrations.AddField(
            model_name='greencheckipapprove',
            name='hostingprovider',
            field=models.ForeignKey(db_column='id_hp', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Hostingprovider'),
        ),
        migrations.AddIndex(
            model_name='greenlist',
            index=models.Index(fields=['url'], name='url'),
        ),
        migrations.AddIndex(
            model_name='greencheckip',
            index=models.Index(fields=['ip_end'], name='ip_eind'),
        ),
        migrations.AddIndex(
            model_name='greencheckip',
            index=models.Index(fields=['ip_start'], name='ip_start'),
        ),
        migrations.AddIndex(
            model_name='greencheckip',
            index=models.Index(fields=['active'], name='active'),
        ),
        migrations.AddIndex(
            model_name='greencheckasn',
            index=models.Index(fields=['active'], name='active'),
        ),
        migrations.AddIndex(
            model_name='greencheckasn',
            index=models.Index(fields=['asn'], name='asn'),
        ),
        migrations.AlterField(
            model_name='greenchecktld',
            name='hps',
            field=models.IntegerField(verbose_name='Hostingproviders registered in tld'),
        ),
        migrations.AlterField(
            model_name='greencheckasnapprove',
            name='action',
            field=models.TextField(choices=[('', 'empty'), ('new', 'new'), ('update', 'update')]),
        ),
        migrations.AlterField(
            model_name='greencheckipapprove',
            name='action',
            field=models.TextField(choices=[('', 'empty'), ('new', 'new'), ('update', 'update')]),
        ),
        migrations.AlterField(
            model_name='greencheckasnapprove',
            name='status',
            field=models.TextField(choices=[('Approved', 'approved'), ('Deleted', 'deleted'), ('New', 'new'), ('Removed', 'removed'), ('Update', 'update')]),
        ),
        migrations.AlterField(
            model_name='greencheckipapprove',
            name='status',
            field=models.TextField(choices=[('Approved', 'approved'), ('Deleted', 'deleted'), ('New', 'new'), ('Removed', 'removed'), ('Update', 'update')]),
        ),
    ]
