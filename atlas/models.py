# Create your models here.
from django.db import models




class SupervisoryFactor(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text="Unique identifier for each record"
    )
    asset_class = models.CharField(
        max_length=255,
        help_text="Name of the asset class (e.g., Interest Rate, Equity, Credit)"
    )
    supervisory_factor = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text="Supervisory factor value (e.g., 0.005)"
    )
    effective_date = models.DateField(
        help_text="The date when this supervisory factor becomes effective"
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when this record was created"
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when this record was last updated"
    )
    remarks = models.TextField(
        null=True,
        blank=True,
        help_text="Additional remarks or regulatory notes"
    )

    class Meta:
        db_table = "supervisory_factors"
        verbose_name = "Supervisory Factor"
        verbose_name_plural = "Supervisory Factors"

    def __str__(self):
        return f"{self.asset_class} - SF: {self.supervisory_factor} (Effective: {self.effective_date})"


class Trade(models.Model):
    trade_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique identifier for the trade"
    )
    netting_set_id = models.CharField(
        max_length=50,
        help_text="Identifier for the netting set to which the trade belongs"
    )

    counterparty_id = models.CharField(
        max_length=50,
        help_text="Identifier for counterparty to which the trade belongs",
        null=True,
        blank=True
    )

    asset_class = models.CharField(
        max_length=50,
        help_text="Asset class of the trade (e.g., Interest Rate, Equity)"
    )
    notional = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        help_text="Notional value of the trade"
    )
    mtm = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        help_text="Mark-to-market value of the trade"
    )
    collateral = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Collateral value associated with the trade"
    )
    is_collateral_posted = models.BooleanField(
        default=False,
        help_text="Indicates if collateral has been posted"
    )
    currency = models.CharField(
        max_length=10,
        default="USD",
        help_text="Currency of the trade"
    )
    market_date = models.DateField(
        help_text="Date when the market value was recorded"
    )
    trade_date = models.DateField(
        help_text="Date when the trade was executed"
    )
    maturity_date = models.DateField(
        help_text="Maturity date of the trade"
    )
    trade_status = models.CharField(
        max_length=20,
        default="Active",
        choices=[
            ("Active", "Active"),
            ("Closed", "Closed"),
            ("Pending", "Pending"),
        ],
        help_text="Status of the trade"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the trade record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the trade record was last updated"
    )

    class Meta:
        db_table = "trades"
        verbose_name = "Trade"
        verbose_name_plural = "Trades"

    def __str__(self):
        return f"Trade {self.trade_id} ({self.asset_class}) - {self.currency}"
