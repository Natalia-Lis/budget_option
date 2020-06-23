from django.contrib import admin
from budget_app.models import (Budget, MonthsBudget, PiggyBanks, Stock, AlreadyCollected,
                               PaymentDay, Credits, Repayment, RepaymentDay)

#
# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ("like", "voting_photo", "voting_user_list")
#     def voting_user_list(self, obj):
#         return ", ".join([str(u) for u in obj.voting_user.all()])
#



@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("name", "money", "monthly", "description")


@admin.register(PiggyBanks)
class PiggyBanksAdmin(admin.ModelAdmin):
    list_display = ("money_for", "m_min", "description")


@admin.register(MonthsBudget)
class MonthsBudgetAdmin(admin.ModelAdmin):
    list_display = ("chosen_name_of_month", "month_cost", "description", "month_date")


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("name", "enter_price", "interests", "value_of",
                    "price", "dividend", "type_of_market", "www")


@admin.register(Credits)
class CreditsAdmin(admin.ModelAdmin):
    list_display = ("name", "credit_amount", "should_end_on", "description")


@admin.register(AlreadyCollected)
class AlreadyCollectedAdmin(admin.ModelAdmin):
    list_display = ("id", "collected")



@admin.register(PaymentDay)
class PaymentDayAdmin(admin.ModelAdmin):
    list_display = ("date_of", "value_of", "payment_piggybanks", "payment_collected")


@admin.register(Repayment)
class RepaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "collected_money")
    def payment_target_list(self, obj):
        return ", ".join([str(u) for u in obj.payment_target.all()])


@admin.register(RepaymentDay)
class RepaymentDayAdmin(admin.ModelAdmin):
    list_display = ("repayment_date", "repayment_value",
                    "repayment_credits", "repayment_collected")

