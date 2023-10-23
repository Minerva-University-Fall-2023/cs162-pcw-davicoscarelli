from models.base import Base, engine
import scripts.insert_data as insert_data
import scripts.query_data as query_data

# Create tables
Base.metadata.create_all(engine)

# Insert data
user_id = insert_data.insert_user("John Doe")
insert_data.insert_transaction(user_id, 100, "Salary")

# Query data
transactions = query_data.get_transactions_by_user_name("John Doe")

# Print results
print("Transactions for John Doe:")
for transaction in transactions:
    print(transaction.description, transaction.amount)

