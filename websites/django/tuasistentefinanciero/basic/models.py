from django.db import models


# Create your models here.
class AppUser(models.Model):
    """Usuario de la aplicación"""
    name = models.CharField(verbose_name="User Name", max_length=150)

    def __str__(self):
        return self.name


class AppGoods(models.Model):
    """Representa los bienes de un usuario"""
    name = models.CharField(verbose_name="Description", max_length=150)
    value = models.DecimalField(verbose_name="Good Value")

    def __str__(self):
        return self.name


class AppDebts(models.Model):
    """Representa las deudas de un usuario"""
    name = models.CharField(verbose_name="Description",max_length=150)
    value = models.DecimalField(verbose_name="Debt Value")

    def __str__(self):
        return self.name


class AppCashbook(models.Model):
    """Movimientos financieros"""
    pass


class AppCategory(models.Model):
    """"""
    pass


class AppCategoryType(models.Model):
    """Categorias: Ingresos o Gastos"""
    name = models.CharField(verbose_name="Category Type Name",max_length=100)

    def __str__(self):
        return  self.name


class AppFinancialStatement(models.Model):
    """"""
    pass

class AppPaymentType(models.Model):
    """"""
    pass