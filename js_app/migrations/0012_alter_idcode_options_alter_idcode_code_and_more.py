# Generated by Django 4.2.1 on 2024-03-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("js_app", "0011_alter_idcode_recognition"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="idcode",
            options={"verbose_name": "ONNX文字识别接口"},
        ),
        migrations.AlterField(
            model_name="idcode",
            name="code",
            field=models.TextField(verbose_name="图片Base64编码"),
        ),
        migrations.AlterField(
            model_name="idcode",
            name="content",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="识别内容"
            ),
        ),
        migrations.AlterField(
            model_name="idcode",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="idcode",
            name="img_url",
            field=models.CharField(
                blank=True, default="", max_length=512, verbose_name="图片地址"
            ),
        ),
        migrations.AlterField(
            model_name="idcode",
            name="recognition",
            field=models.TextField(verbose_name="识别结果"),
        ),
    ]