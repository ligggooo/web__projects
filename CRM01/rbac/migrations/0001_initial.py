# Generated by Django 2.1.5 on 2019-01-28 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='菜单标题')),
                ('icon', models.CharField(max_length=32, verbose_name='菜单图标')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='权限标题')),
                ('url', models.CharField(max_length=128, verbose_name='url正则表达式')),
                ('name', models.CharField(help_text='与url别名相同，可用于反向解析', max_length=32, unique=True, verbose_name='别名')),
                ('menu', models.ForeignKey(blank=True, help_text='null 表示不属于任何菜单，否则属于一个菜单', null=True, on_delete=django.db.models.deletion.PROTECT, to='rbac.Menu', verbose_name='所属菜单')),
                ('pid', models.ForeignKey(help_text='例如：用户删除权限不能做菜单，但是点击这个选项，会使得用户列表这个菜单处于被激活状态', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent', to='rbac.Permission', verbose_name='关联权限')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='拥有的所有权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
        ),
    ]