# from collections import defaultdict
# from datetime import datetime, timedelta
 
# class EnergyBank:
#     def __init__(self, energy_rate=100, decay_rate=0.05):
#         self.energy_rate = energy_rate
#         self.decay_rate = decay_rate
#         self.user_energy = defaultdict(float)  
#         self.user_transaction_history = defaultdict(list)  
 
#     def send_money(self, sender, recipient, amount):
#         now = datetime.now()
#         time_threshold = now - timedelta(days=30)
 
#         recent_transactions = [t for t in self.user_transaction_history[sender] if t[1] >= time_threshold]
#         self.user_transaction_history[sender] = recent_transactions 
 
#         decay_multiplier = (1 - self.decay_rate) ** len(recent_transactions)
#         energy_cost = amount * decay_multiplier
 
#         if self.user_energy[sender] >= energy_cost:
#             self.user_energy[sender] -= energy_cost
#             self.user_transaction_history[sender].append((recipient, now))
#             print(f"Transaction successful! {sender} sent {amount} units to {recipient} using {energy_cost:.2f} energy points.")
#         else:
#             self.convert_to_currency(sender, amount)
#     def convert_to_currency(self, sender, amount):
#         fee = amount * 0.10
#         total_cost = amount + fee
#         print(f"Insufficient energy. Converting to currency. {sender} needs to pay {total_cost:.2f} units (including {fee:.2f} fee).")
 
# bank = EnergyBank()
 
# bank.user_energy["user1"] = 500
# bank.user_energy["user2"] = 300
 
# bank.send_money("user1", "user2", 100)  
# bank.send_money("user1", "user2", 150)  
# bank.send_money("user1", "user2", 300)  


