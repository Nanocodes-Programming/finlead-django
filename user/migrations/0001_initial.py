# Generated by Django 4.1.5 on 2023-01-18 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="InvestmentPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plan_name", models.CharField(blank=True, max_length=50, null=True)),
                ("investment_amount_highest", models.IntegerField(default=0)),
                ("investment_amount_lowest", models.IntegerField(default=0)),
                ("number_of_days", models.IntegerField(default=0)),
                ("investment_profit_percent", models.FloatField(default=0)),
                ("referral_profit_percent", models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="r.jpg",
                        null=True,
                        upload_to="profile_images",
                    ),
                ),
                (
                    "face_image",
                    models.ImageField(
                        blank=True,
                        default="nil.jpg",
                        null=True,
                        upload_to="face_reg_images",
                    ),
                ),
                ("available_balance", models.FloatField(default=0)),
                ("live_profit", models.FloatField(default=0)),
                ("book_balance", models.FloatField(default=0)),
                ("plan_name", models.CharField(blank=True, max_length=50, null=True)),
                ("plan_days", models.IntegerField(blank=True, default=0, null=True)),
                ("plan_end_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("plan_amount", models.IntegerField(blank=True, default=0, null=True)),
                ("referral_price", models.FloatField(default=0)),
                ("referral_people", models.FloatField(default=0)),
                (
                    "referred_by",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default="Blank Name", max_length=50, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="Blank Email", max_length=254, null=True
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, default="Blank Address", max_length=300, null=True
                    ),
                ),
                (
                    "second_address",
                    models.CharField(
                        blank=True, default="Blank Address", max_length=300, null=True
                    ),
                ),
                (
                    "logo",
                    models.ImageField(default="logo.png", upload_to="site_images"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, default="000000000", max_length=50, null=True
                    ),
                ),
                (
                    "owned_by",
                    models.CharField(
                        blank=True, default="Admin", max_length=50, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WalletAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bitcoin_address",
                    models.CharField(
                        blank=True, default="wallet address", max_length=100, null=True
                    ),
                ),
                (
                    "litecoin_address",
                    models.CharField(
                        blank=True, default="wallet address", max_length=100, null=True
                    ),
                ),
                (
                    "xrp_address",
                    models.CharField(
                        blank=True, default="wallet address", max_length=100, null=True
                    ),
                ),
                (
                    "etherum_address",
                    models.CharField(
                        blank=True, default="wallet address", max_length=100, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Withdraw",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("amount", models.IntegerField(default=0)),
                ("wallet_type", models.CharField(max_length=50)),
                ("wallet_address", models.CharField(max_length=100)),
                ("usdt_amount", models.FloatField(default=0)),
                ("verified", models.BooleanField(default=False)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("amount", models.IntegerField(default=0)),
                ("wallet_type", models.CharField(max_length=50)),
                ("wallet_address", models.CharField(max_length=100)),
                ("usdt_amount", models.FloatField(default=0)),
                ("verified", models.BooleanField(default=False)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.TextField(blank=True, null=True)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "action_title",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("category", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Referral",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="referrals",
                        to="user.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PendingDeposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("amount", models.IntegerField(default=0)),
                ("wallet_address", models.CharField(max_length=100)),
                ("wallet_type", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.TextField(blank=True, null=True)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "action_title",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("read", models.BooleanField(default=False)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("amount", models.IntegerField(default=0)),
                ("wallet_type", models.CharField(max_length=50)),
                ("wallet_address", models.CharField(max_length=100)),
                ("usdt_amount", models.FloatField(default=0)),
                ("verified", models.BooleanField(default=False)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.profile"
                    ),
                ),
            ],
        ),
    ]
